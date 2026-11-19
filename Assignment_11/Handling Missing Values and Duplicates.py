# Detect missing values
df.isnull()

# Drop rows with missing values
df.dropna()

# Fill missing values
df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'})

# Remove duplicate rows
df.drop_duplicates()