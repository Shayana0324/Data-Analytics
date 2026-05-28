import pandas as pd

reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)

# Dtypes
print(reviews.price.dtype)
print(reviews.dtypes)
print(reviews.points.astype('float64'))
print(reviews.index.dtype)

# Missing data
print(reviews[pd.isnull(reviews.country)])
print(reviews.region_2.fillna("Unknown"))
print(reviews.taster_twitter_handle.replace("@kerinokeefe", '@kerino'))