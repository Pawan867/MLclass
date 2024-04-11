# from timer import timer


# @timer(1, 1)
# def main():
#     for i in range(100):
#         print(i)

import requests
from time1 import timer

URL = "https://httpbin.org/uuid"


def fetch_uuid(session, url):
    with session.get(url) as response:
        print(response.json())['uuid']


@timer(1, 1)
def main():
    with requests.Session() as session:
        for _ in range(10):
            fetch_uuid(session, URL)
