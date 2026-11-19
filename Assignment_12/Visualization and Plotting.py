import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

# Sample data
data = {
    'Age': [24, 27, 22, 32, 29, 25, 30],
    'Salary': [50000, 60000, 52000, 58000, 62000, 55000, 60000],
}
df = pd.DataFrame(data)

# Histogram
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Box Plot
sns.boxplot(y=df['Age'])
plt.title('Box Plot of Age')
plt.show()

# Scatter Plot
plt.scatter(df['Age'], df['Salary'])
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Correlation Matrix
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()