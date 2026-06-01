import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
landslides = pd.read_csv("./input/catalog.csv")

# set seed for reproducibility
np.random.seed(0)

print(landslides.head())