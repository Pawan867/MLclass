import numpy as np
import pandas as pd
import csv

data_path = 'HR_comma_sep.csv'

df = pd.read_csv(data_path)
# print(df)
# print(df.head())
# print(df.reset_index())
df_hr_ = df.reset_index()
# print(df_hr_)
df_hr_.columns.values[0] = "emp_id"
# print(df_hr_.head())
f_depart = df_hr_[['emp_id', 'Department']]

# drop department from original table
df_hr_.drop('Department', axis=1, inplace=True)

# print(df_hr_.head())
df_inner = pd.merge(df_hr_, f_depart, on='emp_id', how='inner')

print(df_inner.head())
