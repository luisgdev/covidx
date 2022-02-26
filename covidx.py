import sys
import time

import requests


def run():
    # Source URL
    url = "https://corona.lmao.ninja/v2/"

    # Set URL endpoint
    if len(sys.argv) == 1:
        url += "all"
        print("===== COVID19 GLOBAL DATA =====")
    else:
        country = sys.argv[1]
        print(f"==== COVID19 IN {country.upper()} ====")
        url += f"countries/{country}"

    # Request data
    data = requests.get(url).json()

    # Process data
    cases = data["cases"]
    deaths = data["deaths"]
    recovered = data["recovered"]
    deathr = round(deaths / cases * 100, 2)
    recovr = round(recovered / cases * 100, 2)
    tests = data["tests"]
    todayCases = data["todayCases"]
    todayDeaths = data["todayDeaths"]
    active = data["active"]
    critical = data["critical"]
    casesPerOneMillion = data["casesPerOneMillion"]
    deathsPerOneMillion = data["deathsPerOneMillion"]
    testsPerOneMillion = data["testsPerOneMillion"]
    if len(sys.argv) == 1:
        affectedCountries = data["affectedCountries"]

    # Print processed data
    print(f"Total Cases: {cases}")
    print(f"Deaths: {deaths} ({deathr}%)")
    print(f"Recovered: {recovered} ({recovr}%)")
    print("-------------------------")
    print(f"Today Cases: {todayCases}")
    print(f"Today Deaths: {todayDeaths}")
    print("-------------------------")
    print(f"Active Cases: {active}")
    print(f"Critical Cases: {critical}")
    print("-------------------------")
    print(f"Total Tests: {tests}")
    print(f"Tests per Million: {testsPerOneMillion}")
    print(f"Cases per Million: {casesPerOneMillion}")
    print(f"Deaths per Million: {deathsPerOneMillion}")
    print("-------------------------")
    if len(sys.argv) == 1:
        print(f"Affected Countries: {affectedCountries}")
        print("=========================")


def test():
    print(".")
    # Start counting elapsed time
    init_time = time.perf_counter()
    # Run program
    run()
    # Stopt counting elapsed time
    elapsed = round(time.perf_counter() - init_time, 2)
    print(f" *** Elapsed time: {elapsed} s ***\n.")


if __name__ == "__main__":
    test()
