import pandas as pd
import numpy as np

df = pd.read_csv('weather_data.csv')

# df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
# df['windspeed'] = pd.to_numeric(df['windspeed'], errors='coerce')

# df.to_csv('cleaned_weather_data.csv', index=False)
