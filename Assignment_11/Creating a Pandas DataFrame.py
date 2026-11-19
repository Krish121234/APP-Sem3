# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}
df = pd.DataFrame(data)

# Create a DataFrame from a list of dictionaries
data_list = [
    {'Name': 'Alice', 'Age': 24, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 27, 'City': 'Los Angeles'},
]
df_list = pd.DataFrame(data_list)