import requests
from bs4 import BeautifulSoup
import csv
import sqlite3

# Configuration
url = 'https://www.worldometers.info/coronavirus/'
csv_path = r'C:\Users\Asus\Desktop\MLearning Class\Tasks\thirdweektask\3rddaytask\covid_data.csv'
db_path = r'C:\Users\Asus\Desktop\MLearning Class\Tasks\thirdweektask\3rddaytask\covid_data.db'
column_names = [
    "Names",
    "Total Cases",
    "New Cases",
    "Total Deaths",
    "New Deaths",
    "Total Recovered",
    "New Recovered",
    "Active Cases",
    "Serious Cases",
    "Total Tests",
    "Population"
]

# Fetch and parse webpage
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
table_rows = soup.find('table').find_all('tr')[8:]

# Extract data and ensure each row matches the specified columns
data = [[td.text.strip() for td in tr.find_all('td')] for tr in table_rows]
# Filter rows to match column count
data = [row for row in data if len(row) == len(column_names)]

# Save data to CSV, including column headers
with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(column_names)  # Write column names as the header
    writer.writerows(data)

# Save data to SQLite DB
conn = sqlite3.connect(db_path)
cur = conn.cursor()
# Drop existing table if necessary
cur.execute('DROP TABLE IF EXISTS covid_data')
columns = ', '.join(
    [f'"{name}" TEXT' for name in column_names])  # Define columns
# Create table with specified columns
cur.execute(f'CREATE TABLE covid_data ({columns})')
insert_query = 'INSERT INTO covid_data VALUES (' + ','.join(
    ['?'] * len(column_names)) + ')'  # Prepare insert query
cur.executemany(insert_query, data)  # Insert data
conn.commit()
conn.close()

print('Data saved to CSV and SQLite DB with specified columns.')
