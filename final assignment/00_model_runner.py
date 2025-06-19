import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from ema_workbench import (
    Model,
    Policy,
    ema_logging,
    SequentialEvaluator,
    MultiprocessingEvaluator,
)

from dike_model_function import DikeNetwork  # @UnresolvedImport
from problem_formulation import get_model_for_problem_formulation, sum_over, sum_over_time

import os 
import pickle

# CONFIGURE
RUN_NAME = "A.1_heightening"

if __name__ == "__main__":
    ema_logging.log_to_stderr(ema_logging.INFO)
    # choose problem formulation number, between 0-5
    # each problem formulation has its own list of outcomes
    dike_model, planning_steps = get_model_for_problem_formulation(5)
    print(dike_model.outcomes)

    # pass the policies list to EMA workbench experiment runs
    EXP_PATH = f"./saved_runs/{RUN_NAME}_exp.pkl"
    OUT_PATH = f"./saved_runs/{RUN_NAME}_out.pkl"

    def get_do_nothing_dict():
        return {l.name: 0 for l in dike_model.levers}

    # CONFIGURE
    custom_policies = [
        Policy( "Upstream Response", 
            **dict(
                get_do_nothing_dict(),
                **{"A.1_DikeIncrease 0": 10}
            )
        )
    ]

    # creating model
    if not os.path.exists(EXP_PATH):
        with MultiprocessingEvaluator(dike_model) as evaluator:
            results = evaluator.perform_experiments(scenarios=2500, policies=custom_policies)
            experiments, outcomes = results
            # only works because we have scalar outcomes
            outcome_df = outcomes
            experiments_df = experiments

        # saving files
        with open(EXP_PATH, "wb") as file:
            pickle.dump(experiments_df, file)
        with open(OUT_PATH, "wb") as file:
            pickle.dump(outcome_df, file)

    else:
        print("<< File exists already >>")
        with open(EXP_PATH, "rb") as file:
            experiments_df = pickle.load(file)
        with open(OUT_PATH, "rb") as file:
            outcome_df = pickle.load(file)

    print("done")