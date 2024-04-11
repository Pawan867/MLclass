# Data Frame Data Frame
# import numpy as np
# import pandas as pd
# import csv

# data_path = ''

# df = pd.read_csv(data_path)

import csv
import pandas as pd
import numpy as np
df_dict = {
    "name": [1, 2, 3, 4, 5, 6, 7],
    "age": [90, 80,  70, 60, 50, 40, 30],
    "address": ["a", "b", "c", "d", "e", "f", "g"]
}

df_dict_list = [
    {
        "name": [1, 2, 3, 4, 5, 6, 7],
        "age": [90, 80,  70, 60, 50, 40, 30],
        "address": ["a", "b", "c", "d", "e", "f", "g"]
    }
]
df_dict_tupple = (
    {
        "name": [1, 2, 3, 4, 5, 6, 7],
        "age": [90, 80,  70, 60, 50, 40, 30],
        "address": ["a", "b", "c", "d", "e", "f", "g"]
    }
)

df_list_list = [[1, 90, "a"], [2, 80, "b"], [3, 70, "c"], [
    4, 60, "d"], [5, 50, "e"], [6, 40, "f"], [7, 30, "g"]]

# def create_dataframe():
#     """Create a dataframe using the dictionary."""
#     return pd.DataFrame(df_dict)

# def append_rows():
#     """Append rows to an existing dataframe."""
#     global df

#     new_row = {'name': 8, 'age': 70, 'address': 'h'}
# df = pd.read_csv(df_dict)
# print(df)
# Question:
# <li>Read 'weather_data.csv' file using csv reader.</li>
# <li>Store the data inside the csv file into a list of lists.</li>
# <li>Then create a pandas dataframe using list of list.</li>
data_path = './weather_data.csv'
df = pd.read_csv(data_path, sep='\t')
df1 = pd.read_csv(data_path, on_bad_lines='skip')
# df2 = pd.read_csv(data_path, header=None, names=['Column1', 'Column2'])
print(df)

# df_drop = df1.drop()
# print(df_drop.head())


# Question
# <li>1. Read 'imports-85.data' file using file reader.</li>
# <li>2. Store the data present inside the file into a list of list.</li>
# <li>3. Create a pandas dataframe using list of lists.</li>
# <li>4. For column name, we can use the columns variable given below.</li>


# import_columns = ['symboling', 'normalized_losses', 'make', 'fuel_type', 'aspiration', 'num_of_doors',
#           'body_style', 'drive_wheels', 'engine_location', 'wheel_base', 'length', 'width',
#            'height', 'curb_weight', 'engine_type', 'num_of_cylinders', 'engine_size', 'fuel_system',
#           'bore', 'stroke', 'compression', 'horsepower', 'peak_rpm', 'city_mpg', 'highway_mpg',
#            'price']


# Question:
# Reading a CSV file using skiprows and header parameters


weather_df = pd.read_csv('weather_data.csv', skiprows=[1], header=2)
print(weather_df)


# pd. pivot table
