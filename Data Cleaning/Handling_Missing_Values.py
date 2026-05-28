import pandas as pd
import numpy as np

# Real in all our data
nfl_data = pd.read_csv("./input/NFL Play by Play 2009-2016 (v3).csv")

# set seed for reproducibility
print(np.random.seed(0))
print(nfl_data.head())

# Get the number of missing data points per column
missing_values_count = nfl_data.isnull().sum()
# Look at the number of missing points in the firs ten columns
print(missing_values_count[0:10])
# How many total missing values do we have?
total_cells = np.product(nfl_data.shape)
total_missing = missing_values_count.sum()

# Percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)