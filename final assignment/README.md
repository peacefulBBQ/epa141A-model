# EPA-simmodel

# jdnjoas

# Things to do

- Find literature or some other form of reference to define uncertainties

## Things to check

- Does it make sense to build the Dikes up at a later time step?
- Probably not

## Policy problem

Use Jupyter Notebook named "Problem Formulation varying policies" to visualize costs accross various policies.

## Global Sensitivity Analysis

1. Correlation matrices in the uncertainty space and policy space
  Use Jupyter Notebook named "Problem Formulation sensitivity".

3. Sobol indices
   Use Jupyter Notebook named "Problem Formulation sobol".

## Starting with Scenario discovery

- Visualization of initial values of different dike rings in comparison?

- What uncertainties lead to what unfavorable outcomes




## Robustness Measures

# Complimentary file needed to run the model
- problem_formulation.py
- dike_model_function.py
- all the original file from original folder given from EPA141A-open

# What does it do?
- set the policy (taken from directed search policy steps)
- run the model using EMA workbench with 2500 scenarios
- save the outcomes
- calculate maximum regret for local and national perspective
- plot the maximum regret

# Save file 
- model file: final assignment/Robustness Measures.ipynb
- images: final assignment/saved_runs/robustness_measures/image
- outcomes and scenario of experiments: final assignment/saved_runs/robustness_measures
