import pandas as pd
import matplotlib.pyplot as plt
from ema_workbench import Policy, perform_experiments
from problem_formulation import get_model_for_problem_formulation
from dike_model_function import DikeNetwork


def create_policy(name, dike_increase, rfr_projects, days_to_threat, planning_steps, dike_model):

    policy_dict = {}

    # Set dike increases
    for dike in dike_model.function.dikelist:
        for step in planning_steps:
            policy_dict[f"{dike}_DikeIncrease {step}"] = dike_increase

    # Set RfR projects
    for project in range(5):  # There are 5 RfR projects
        for step in planning_steps:
            policy_dict[f"{project}_RfR {step}"] = rfr_projects[project] if project < len(rfr_projects) else 0

    # Set EWS days to threat
    policy_dict["EWS_DaysToThreat"] = days_to_threat

    return Policy(name, **policy_dict)


def analyze_policy_costs(results):

    # Convert results to DataFrame
    experiments, outcomes = results
    df = pd.concat([experiments, pd.DataFrame(outcomes)], axis=1)

    # Extract cost components
    cost_components = [col for col in df.columns if 'Cost' in col or 'Damage' in col]

    # Calculate total costs
    df['Total Costs'] = df[cost_components].sum(axis=1)

    # Group by policy and calculate mean costs
    policy_costs = df.groupby('policy')[cost_components + ['Total Costs']].mean()


    policy_costs = policy_costs.sort_values('Total Costs', ascending=False)


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Bar plot of total costs by policy
    policy_costs['Total Costs'].plot(kind='bar', ax=ax1, title='Total Costs by Policy')
    ax1.set_ylabel('Costs (million €)')
    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    # Stacked bar plot of cost components
    policy_costs[cost_components].plot(kind='bar', stacked=True, ax=ax2,
                                       title='Cost Breakdown by Policy')
    ax2.set_ylabel('Costs (million €)')
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()

    return policy_costs


if __name__ == "__main__":
    # Initialize
    dike_model, planning_steps = get_model_for_problem_formulation(2)  # Using PF2 for detailed cost breakdown

    # Define policies to test
    policies = [
        create_policy("Do Nothing",
                      dike_increase=0,
                      rfr_projects=[0, 0, 0, 0, 0],
                      days_to_threat=0,
                      planning_steps=planning_steps,
                      dike_model=dike_model),

        create_policy("Minimal Protection",
                      dike_increase=2,
                      rfr_projects=[0, 0, 0, 0, 0],
                      days_to_threat=1,
                      planning_steps=planning_steps,
                      dike_model=dike_model),

        create_policy("Moderate Protection",
                      dike_increase=5,
                      rfr_projects=[0, 1, 0, 0, 0],
                      days_to_threat=2,
                      planning_steps=planning_steps,
                      dike_model=dike_model),

        create_policy("High Protection",
                      dike_increase=8,
                      rfr_projects=[1, 1, 0, 0, 0],
                      days_to_threat=3,
                      planning_steps=planning_steps,
                      dike_model=dike_model),

        create_policy("Maximum Protection",
                      dike_increase=10,
                      rfr_projects=[1, 1, 1, 1, 1],
                      days_to_threat=4,
                      planning_steps=planning_steps,
                      dike_model=dike_model)
    ]

    # Run experiments
    n_scenarios = 10  # Number of scenarios to test per policy
    results = perform_experiments(dike_model, policies=policies, scenarios=n_scenarios)

    # Analyze and visualize results
    cost_analysis = analyze_policy_costs(results)

    # Print cost summary
    print("\nPolicy Cost Summary (in million €):")
    print(cost_analysis.to_string(float_format="{:,.2f}".format))

    # Calculate cost-effectiveness (cost per life saved)
    if 'Expected Number of Deaths' in results[1]:
        # Extract deaths as a Series
        deaths = pd.DataFrame(results[1])['Expected Number of Deaths']

        # Group by policy and calculate mean deaths
        mean_deaths = deaths.groupby(results[0]['policy']).mean()

        # Add mean deaths to cost_analysis
        cost_analysis['Expected Number of Deaths'] = mean_deaths

        # Compute cost per life saved
        cost_analysis['Cost per Life Saved'] = cost_analysis['Total Costs'] / cost_analysis['Expected Number of Deaths']

        # Display cost-effectiveness summary
        print("\nCost-Effectiveness:")
        print(cost_analysis[['Total Costs', 'Expected Number of Deaths', 'Cost per Life Saved']]
              .sort_values('Cost per Life Saved')
              .to_string(float_format="{:,.2f}".format))