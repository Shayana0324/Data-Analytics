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
total_cells = np.prod(nfl_data.shape)
total_missing = missing_values_count.sum()

# Percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)

# Finding out why the data is missing
# imputation

# Drop missing values
# Remove all the rows that contain a missing value
# print(nfl_data.dropna())  
# Remove all columns with at least one value missing
columns_with_na_dropped = nfl_data.dropna(axis=1)
print(columns_with_na_dropped.head())

# Just how much data did we lose?
print("Columns in original dataset: %d \n" % nfl_data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

# Filling in missing values automatically
# Get a small subset of the NFL dataset
subset_nfl_data = nfl_data.loc[:, 'EPA':'Season'].head()
print(subset_nfl_data)
# Replace all NA's with 0
print(subset_nfl_data.fillna(0))
# Replace all NA's the value that comes dierctly after it in the same column,
# then replace all the remaining na's with 0
print(subset_nfl_data.fillna(method='bfill', axis=0).fillna(0))