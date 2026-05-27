import pandas as pd

reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)

# Summary Functions
print(reviews.points.describe())
print(reviews.taster_name.describe())
print(reviews.points.mean())
print(reviews.taster_name.unique())
print(reviews.taster_name.value_counts())

# Maps
'''In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later. Maps are what handle this work, making them extremely important for getting your work done!
'''
# map()
review_points_mean = reviews.points.mean()
print(reviews.points.map(lambda p: p - review_points_mean))

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

print(reviews.apply(remean_points, axis='columns'))
print(reviews.head(1))

reviews_points_mean = reviews.points.mean()
print(reviews.points - review_points_mean)
print(reviews.country + " - " + reviews.region_1)