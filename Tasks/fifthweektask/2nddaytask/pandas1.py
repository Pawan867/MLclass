import numpy as np
import pandas as pd

# data = [10, 20, 30, 40, 50]
# print(type(data))
# df = pd.Series(data)
# print(df)
# print(type(df))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# df = pd.Series(thisdict)
# print(df)
# print(type(df))

# data = [10, 20, 30, 40, 50]
# da = np.array(data)
# print(da)
# df = pd.Series(da)
# print(type(da))
# print(df)
# print(type(df))


# Create Data From:
# pd.DataFrame()


## data = ([[10, 20, 30, 40, 50]])
# data = [[10, 20], [30, 40], [50, 60]]
# pa = pd.DataFrame(data)
# print(len(data))
# print(pa)

# df_list = pd.DataFrame(data, columns=['col1', 'col2'])

# print(df_list)
# dictionary of list
# dict = {
#     "brand": ["Mercedes", "BMW", "Audi"],
#     "model": ["M6", "M8", "M9"],
#     # "year": 1996
# }

# pa = pd.DataFrame(dict)
# print(len(dict))
# print(pa)

# List of dictionary
# dict1 = [{
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# ]
# pa = pd.DataFrame(dict1)
# print(len(dict1))
# print(pa)


data_path = pd.read_csv("car_details.csv")
df_hr = pd.read_csv(data_path)
df_hr.head()
df_hr.tail()
df_hr.shape()
df_hr.columns()
df_hr.dtypes()
df_hr.to_numpy()
df_hr.info()
df_hr.describe()

print(df_hr)
