import pandas as pd

# Create a Series from a list
ser = pd.Series([10, 20, 30, 40, 50])

# Create a Series with a custom index
ser_custom = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])