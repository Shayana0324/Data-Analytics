import pandas as pd

reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)
# print(reviews)
# print(reviews.country)
print(reviews['country'])
print(reviews['country'][0])

# Indexing in Pandas

# Index-based selection
print(reviews.iloc[0])
print(reviews.iloc[:3, 0])
print(reviews.iloc[1:3, 0])
print(reviews.iloc[[0, 1, 2], 0])
print(reviews.iloc[-5:])

# Label-based selection
print(reviews.loc[0, 'country'])
# iloc is conceptually simpler than loc because it ignores the dataset's indices. 
'''
When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by position. loc, by contrast, uses the information in the indices to do its work. 
'''

print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

# Choosing between loc and iloc
'''
iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
'''

# Manipulating the index
print(reviews.set_index("title"))

# Conditional selection
print(reviews.country == 'Italy')
print(reviews.loc[reviews.country == 'Italy'])
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])

# built-in conditional selector --- isin
print(reviews.loc[reviews.country.isin(['Italy', 'France'])])
# built-in conditional selector --- isnull & notnull
print(reviews.loc[reviews.price.notnull()])

# Assigning data
reviews['critic'] = 'everyone'
print(reviews['critic'])

reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])