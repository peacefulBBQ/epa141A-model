import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import pickle

from ema_workbench import (
    Model,
    Policy,
    ema_logging,
    SequentialEvaluator,
    MultiprocessingEvaluator,
)
from dike_model_function import DikeNetwork  # @UnresolvedImport
from problem_formulation import get_model_for_problem_formulation, sum_over, sum_over_time

from ema_workbench.analysis import prim
from ema_workbench.analysis import scenario_discovery_util as sdutil

# ATTENTION: This script is supposed to be executed from the final_assignment folder 

# CONFIGURE HERE
RUN_NAME = "base_case"
SAVE_ADDITION = "_A.4_Deaths"
label = 'A.4_Expected Number of Deaths'
EXP_PATH = f"./saved_runs/{RUN_NAME}_exp.pkl"
OUT_PATH = f"./saved_runs/{RUN_NAME}_out.pkl"
formulation_num = 5


ema_logging.log_to_stderr(ema_logging.INFO)

# necessary to get for data cleaning later
dike_model, planning_steps = get_model_for_problem_formulation(formulation_num)

with open(EXP_PATH, "rb") as file:
    experiments_df = pickle.load(file)
with open(OUT_PATH, "rb") as file:
    outcome_df = pickle.load(file)

# Necessary to resolve aggregation over time
# ATTENTION: Only works sensibly with planning step == 1
if formulation_num == 5:
    outcome_df = pd.DataFrame({k: v.flatten() for k, v in outcome_df.items()})

cleaned_experiments = experiments_df.drop(labels=[l.name for l in dike_model.levers], axis=1)

data = outcome_df[label]
threshold = data.quantile(0.9)
y = data >= threshold

prim_alg = prim.Prim(cleaned_experiments,y, threshold=0.5)
box1 = prim_alg.find_box()

box1.show_pairs_scatter()
plt.tight_layout()
plt.savefig(f"./saved_figures/{RUN_NAME}_prim_scatter{SAVE_ADDITION}.png")
plt.close()

box1.inspect(style="graph")
plt.tight_layout()
plt.savefig(f"./saved_figures/{RUN_NAME}_prim_box_values{SAVE_ADDITION}.png")
plt.close()


