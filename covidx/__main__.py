"""Covidx main module"""

import sys
from pprint import pprint
from timeit import timeit

import requests
from requests import Request

from covidx import views
from covidx.models import API


def _get_data(url: str) -> dict:
    """
    Get data from API.
    :param url: URL endpoint.
    :return: Dict with data.
    """
    data: dict = {}
    try:
        data: Request = requests.get(url=url, timeout=30)
        return data.json()
    except Exception as ex:
        print(f"Error: {ex}")
        pprint(data)
        sys.exit()


def controller() -> None:
    """
    Handle user input.
    :return: None
    """
    if len(sys.argv) == 1:
        url: str = API.all_
        print("===== COVID19 GLOBAL DATA =====")
    else:
        country = sys.argv[1]
        print(f"==== COVID19 IN {country.upper()} ====")
        url = API.country + country
    data = _get_data(url=url)
    views.show_data(data=data)


def main() -> None:
    """
    Main Interface
    :return: None
    """
    elapsed = timeit(controller, number=1)
    print(f" *** Elapsed time: {round(elapsed, 4)} s ***\n.")


if __name__ == "__main__":
    main()
