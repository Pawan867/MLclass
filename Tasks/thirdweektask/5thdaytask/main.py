import requests
import multiprocessing
from multiprocessing import Pool
from fetch import fetch_uuid
from timer import timer

URL = "https://httpbin.org/uuid"


@timer(1, 1)
def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch_uuid, [(session, URL) for _ in range(100)])


if __name__ == '__main__':
    main()
