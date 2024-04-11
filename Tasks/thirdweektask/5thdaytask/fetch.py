import requests

def fetch_uuid(session, url):
    with session.get(url) as response:
        try:
            json_data = response.json()
            if 'uuid' in json_data:
                print(json_data['uuid'])
            else:
                print("No 'uuid' found in response:", json_data)
        except ValueError:
            print("Invalid JSON response:", response.text)
