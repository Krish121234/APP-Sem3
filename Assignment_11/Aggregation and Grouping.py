data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 52000, 58000]
}
df = pd.DataFrame(data)

# Group by department and calculate average salary
grouped = df.groupby('Department')
avg_salary = grouped['Salary'].mean()

# Aggregate multiple functions
grouped['Salary'].agg(['mean', 'sum', 'max'])