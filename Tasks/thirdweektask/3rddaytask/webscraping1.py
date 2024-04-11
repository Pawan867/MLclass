# import requests
# from bs4 import BeautifulSoup
# import csv
# import sqlite3

# # Define URL, CSV path, and SQLite DB path
# url = 'https://www.worldometers.info/coronavirus/'
# csv_path = r'C:\Users\Asus\Desktop\MLearning Class\Tasks\thirdweektask\3rddaytask\covid_data.csv'
# db_path = r'C:\Users\Asus\Desktop\MLearning Class\Tasks\thirdweektask\3rddaytask\covid_data.db'

# # Fetch and parse the HTML
# soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# rows = soup.find('table').find_all('tr')[8:]

# # Process table rows
# data = [[col.text.strip() for col in row.find_all('td')]
#         for row in rows if row.find_all('td')]

# # Save to CSV
# with open(csv_path, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# # Save to SQLite
# conn = sqlite3.connect(db_path)
# c = conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS covid_data (' +
#           ', '.join([f'col{i} TEXT' for i in range(len(data[0]))]) + ')')
# c.executemany('INSERT INTO covid_data VALUES (' +
#               ', '.join(['?']*len(data[0])) + ')', data)
# conn.commit()
# conn.close()

# print(f'Data saved to {csv_path} and SQLite DB at {db_path}')
