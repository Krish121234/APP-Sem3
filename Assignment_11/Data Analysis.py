# Load the Data
df = pd.read_csv('employees.csv')
print(df.head())

# Clean the Data
# Remove rows with any missing values
df_cleaned = df.dropna()

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

# Fill missing numerical values with the mean
df_cleaned['Age'].fillna(df_cleaned['Age'].mean(), inplace=True)