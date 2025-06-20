# EPA141 - Group project

Nina Kerff 6271707
Adli Luthfi 6140548
Adithya Santhosh Kumar 6231292
Ben Schäfer 6314805

This README complements the report of our group and provides additonal
information on the methodology and how we created the figures used in the
report.

This repository is built on top of the model provided as part of the course. The
additional added code and analysis is divided along the lines of the different
used analysis methods used in the report.

## Requirements for working with this repository

If you have used specific packages or have a weird setup which might make it
hard for others to run: mention it here or change them yourself

## Policy problem

The script and figure showing the costs related to the different policies can be found in the PolicyProblem_Costs folder of the final assignment.
Use Jupyter Notebook named "Problem Formulation varying policies" to visualize costs accross various policies.

## Global Sensitivity Analysis

1. Correlation matrices in the uncertainty space and policy space:
   The script and figure showing the correlation matrices can be found in the SensitivityAnalysis folder of the final assignment.
   Use Jupyter Notebook named "Problem Formulation sensitivity" to run the figures again.

2. Sobol indices:
   The script, saved data and figures showing Sobol indices can be found in the SensitivityAnalysis folder of the final assignment.
   Use Jupyter Notebook named "Problem Formulation sobol".

## Prim

### Scripts

The scripts used to conduct the subspace partitioning regarding deaths in the
report can be found in the folder `00_prim`. While the report focuses only on
the analysis of the regions Deventer and Zutphen (respective notebooks
`subspace_partitioning_Deventer` and `subspace_partitioning_Zutphen`) additional
analysis of the regions of Gorssel and Doesburg can be found there as well.

The complementary `prim_saver` script provides an additional way of running the
analysis automatically and creating figures. This has not been used to provide
results for the report though and has been only used exploratively.

### Inputs

These scripts do not run the simulation themselves but only visualize results
from already existing runs. They access the simulation results saved in
`saved_runs`under `base_case_exp.pkl`and `base_case_out.pkl`, which are the
outcomes and experiments used. These runs were conducted by running the
`00_model_runner.py` script.

### Outputs

PRIM was conducted to generating worst-case reference scenarios for the later
directed search these results are saved in `saved_runs/reference_cases` with the
names `worst_case_deventer.pkl` and `worst_case_zutphen.pkl`

## Directed Search

### Scripts

The scripts to run the directed search can be found in `01_directed_search` as
`01_directed_search_deventer` and `02_directed_search_zutphen`. These scripts
produce the data sets that are used then in `03_directed_search_visualization`
for creating the plots for the report.

### Inputs

The respective scenarios from the PRIM outputs are used by the scripts.

### Outputs

Besides the figures that can be found in the notebook itself, a few policies are
sampled from the pareto-front of both searches and saved in
`saved_runs/directed_search` under `search_worst_case_deventer.pkl` and
`search_worst_case_zutphen.pkl`.

## Robustness

Where are the relevant scripts?
Where are results saved?
Where can the figures be found which are used in the report?

### Scripts
 
The scripts to run the robustness measures can be found in `Robustness Measures.ipynb`. 
These scripts run the model to calculate maximum regret between different policies.
The outcomes are saved to prevent a need to re-run the model. Additional data 
processing related to local and national perspective, as well as plotting can 
also be found.

### Inputs

The respective scenarios from the Directed Search Policy outputs
are used by the scripts.

### Output
All outputs related to Robustness are saved in folder `saved_runs/robustness_measures`.
The outcomes are saved in `outcomes.pkl`, while scenarios used to run the model are 
saved in `experiments.pkl`. Plot results are saved in `saved_runs/robustness_measures/image`
