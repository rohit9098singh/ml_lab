import sklearn as sk
from sklearn import datasets
import pandas as pd

# Correct version check
print('version of sci-kit learn:', sk.__version__)

# Load iris dataset from sklearn
iris = datasets.load_iris()

# Create DataFrame using iris.data and feature names as columns
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Print the entire dataframe
print(df)

# Print only column names
print(df.columns)

# Show statistical summary (mean, std, min, max, etc.)
print(df.describe())

# Print info about DataFrame (rows, columns, data types, etc.)
print(df.info())

# Show first 5 rows
print(df.head())

# Show last 5 rows
print(df.tail())


