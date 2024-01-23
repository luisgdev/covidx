"""Covidx main module"""

import sys
from pprint import pformat

import requests
from pydantic import ValidationError
from requests import Response

from covidx import views
from covidx.models import CovidApi


def _get_data(url: str) -> dict:
    """
    Get data from API.
    :param url: URL endpoint.
    :return: Dict with data.
    """
    try:
        data: Response = requests.get(url=url, timeout=30)
        return data.json()
    except ValidationError as ex:
        print(f"Error: {pformat(ex)}")
        sys.exit()


def main() -> None:
    """
    Main Interface
    :return: None
    """
    if len(sys.argv) == 1:
        url: str = CovidApi.ALL_
        print("===== COVID19 GLOBAL DATA =====")
    else:
        country = sys.argv[1]
        print(f"==== COVID19 IN {country.upper()} ====")
        url = CovidApi.COUNTRIES_ + country
    data = _get_data(url=url)
    views.show_data(data=data)


if __name__ == "__main__":
    main()
