import pandas as pd

# Load CSV file (Iris dataset)
df = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\ML LAB PROGRAMS\dataset\iris_dataset.csv")

# NOTE: If you haven't already:
# install Excel support using this in CMD: python -m pip install openpyxl

# Load Excel file (Wine dataset)
df1 = pd.read_excel(r"C:\Users\rohit\OneDrive\Desktop\ML LAB PROGRAMS\dataset\wine.xlsx")

# -- COLUMN NAMES --
print("columns of df")
print(df.columns)

print("columns of df1")
print(df1.columns)

# -- DESCRIPTIVE STATS --
print("describe of df")
print(df.describe())   # gives mean, std, min, max for numeric columns

print("describe of df1")
print(df1.describe())

# -- FIRST 5 ROWS (HEAD) --
print("head of df")
print(df.head())       # () is required to see the output!

print("head of df1")
print(df1.head())
