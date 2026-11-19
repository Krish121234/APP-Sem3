from scipy.stats import zscore
import pandas as pd

# Sample data with outliers
data = {
    'Age': [24, 27, 22, 32, 29, 25, 100],  # 100 is an outlier
    'Salary': [
        50000,
        60000,
        52000,
        58000,
        62000,
        55000,
        600000,
    ],  # 600000 is an outlier
}
df = pd.DataFrame(data)

# Detecting outliers using z-scores
df['Age_zscore'] = zscore(df['Age'])
df['Salary_zscore'] = zscore(df['Salary'])
print(df)

# Removing outliers (z-score threshold <= 3)
df_no_outliers = df[
    (df['Age_zscore'].abs() <= 3) & (df['Salary_zscore'].abs() <= 3)
]
print(df_no_outliers)


# Capping outliers function
def cap_values(series):
  upper_limit = series.mean() + 3 * series.std()
  lower_limit = series.mean() - 3 * series.std()
  return series.clip(lower=lower_limit, upper=upper_limit)