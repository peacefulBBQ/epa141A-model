
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import pickle
import os, sys

from ema_workbench import (
    Model,
    Policy,
    ema_logging,
    SequentialEvaluator,
    MultiprocessingEvaluator,
)
from dike_model_function import DikeNetwork  # @UnresolvedImport
from problem_formulation import get_model_for_problem_formulation, sum_over, sum_over_time




# make sure pandas is version 1.0 or higher
# make sure networkx is verion 2.4 or higher
print(pd.__version__)
print(nx.__version__)

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.insert(0, parent_dir)
# os.chdir("..")

ema_logging.log_to_stderr(ema_logging.INFO)
os.chdir("/Users/benschaefer/Desktop/epa141-model/final assignment")
print(os.getcwd())
# choose problem formulation number, between 0-5
# each problem formulation has its own list of outcomes
dike_model, planning_steps = get_model_for_problem_formulation(1)

with MultiprocessingEvaluator(dike_model) as evaluator:
            results = evaluator.optimize(
                nfe=200,
                searchover='levers',
                # reference=scenario1,
                epsilons=[0.1] * len(dike_model.outcomes),
                # convergence=convergence_metrics,
                # constraints=constraints
            )