import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

# Sample data
data = {
    'marks': [8, 4, 6, np.nan, 8, 9],
    'sec': ['a', 'b', 'c', np.nan, 'a', 'a'],
    'color': ['red', 'blue', 'green', 'pink', 'voilet', 'orange'],
    'juice': ['mango', 'strawberry', 'lemon', 'butterfruit', 'apple', 'waterlmelon']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# 1. Handle Missing Values
df['marks'] = SimpleImputer(strategy='mean').fit_transform(df[['marks']])
df['sec'] = SimpleImputer(strategy='most_frequent').fit_transform(df[['sec']]).ravel()

# 2. Label Encode 'color' (ordinal style)
df['color'] = LabelEncoder().fit_transform(df['color'])

# 3. One-Hot Encode 'juice' (nominal style)
juice_encoded = OneHotEncoder(sparse_output=False).fit_transform(df[['juice']])
juice_df = pd.DataFrame(juice_encoded, columns=OneHotEncoder(sparse_output=False).fit(df[['juice']]).get_feature_names_out(['juice']))
df = pd.concat([df.drop('juice', axis=1), juice_df], axis=1)

# 4. Standard Scaling 'marks' and 'color'
df[['marks', 'color']] = StandardScaler().fit_transform(df[['marks', 'color']])

print("\nProcessed Data:\n", df)
