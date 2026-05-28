import pandas as pd

reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)

# Renaming
# rename()
print(reviews.rename(columns={'points': 'score'}))
print(reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}))
# set_index(), rename_axis()
print(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))

# Combining
# concat(), join(), merge()
canadian_youtube = pd.read_csv("./CAvideos.csv")
british_youtube = pd.read_csv("./GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date']) 
left.join(right, lsuffix='_CAN', rsuffix='_UK')
