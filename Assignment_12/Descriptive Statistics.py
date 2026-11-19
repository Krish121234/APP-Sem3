import pandas as pd

# Sample data
data = {'Age': [24, 27, 22, 32, 29, 25, 30]}
df = pd.DataFrame(data)

# Descriptive statistics
print(df.describe())
print("Mean:", df['Age'].mean())
print("Median:", df['Age'].median())
print("Mode:", df['Age'].mode()[0])
print("Standard Deviation:", df['Age'].std())
print("Variance:", df['Age'].var())
print("Minimum:", df['Age'].min())
print("Maximum:", df['Age'].max())
print("Quantiles:", df['Age'].quantile([0.25, 0.5, 0.75]))