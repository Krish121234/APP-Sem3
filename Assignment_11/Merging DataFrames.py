df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [3, 4, 5], 'Age': [24, 27, 22]})

# Merge on a common column (Inner Join)
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Different types of joins
left_join = pd.merge(df1, df2, on='ID', how='left')
right_join = pd.merge(df1, df2, on='ID', how='right')
outer_join = pd.merge(df1, df2, on='ID', how='outer')