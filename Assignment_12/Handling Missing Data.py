import pandas as pd

# Sample data with missing values
data = {
    'Age': [24, 27, None, 32, 29, 25, None],
    'Salary': [50000, 60000, 52000, None, 62000, 55000, 60000],
}
df = pd.DataFrame(data)

# Detecting missing values
print(df.isnull())

# Removing rows with missing values
df_dropped = df.dropna()
print(df_dropped)

# Filling missing values with the mean
df_filled = df.fillna(df.mean())
print(df_filled)