import numpy as np
import pandas as pd
import csv

data_path = 'HR_comma_sep.csv'

df = pd.read_csv(data_path)
# print(df)
# print(df.head(10))    

# print(df.shape)
# print(df.index)
# print(df.columns)
# print(df.dtypes)
# print(df.rename(columns={
# 'last_evaluation': 'le'
# })
# )
# print(df.dtypes)
# print(df.values)
# print(df.to_numpy())
# print(df.info())
# print(df.describe())
print(
    df.describe(exclude=['int', 'float']))
