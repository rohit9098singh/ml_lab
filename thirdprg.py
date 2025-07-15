from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,Normalizer
import pandas as pd

data = {"speed": [10, 20, 30, 40, 50], "distance": [1000, 2000, 3000, 4000, 5000]}
df = pd.DataFrame(data)


ss = StandardScaler()
x1 = ss.fit_transform(df)
print(x1)


mm = MinMaxScaler()
x2 = mm.fit_transform(df)  #Pehle data ko analyze karo (fit), fir usi analysis se transform karo"
print(x2)


rs = RobustScaler()
x3 = rs.fit_transform(df)
print(x3)


n = Normalizer()
x4 = n.fit_transform(df)
print(x4)
