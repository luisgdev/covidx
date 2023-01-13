"""Views module"""

from covidx.models import Global


def show_data(data: dict) -> None:
    """Show data"""
    info: Global = Global(**data)
    output: tuple(str) = (
        f"Total Cases: {info.cases} ({round(info.cases/info.population*100, 2)}%)",
        f"Deaths: {info.deaths} ({round(info.deaths/info.cases*100, 2)}%)",
        f"Recovered: {info.recovered} ({round(info.recovered/info.cases*100, 2)}%)",
        f"Population: {info.population}",
        "-" * 25,
        f"Today Cases: {info.today_cases}",
        f"Today Recovered: {info.today_recovered}",
        f"Today Deaths: {info.today_deaths}",
        "-" * 25,
        f"Active Cases: {info.active}",
        f"Critical Cases: {info.critical}",
        "-" * 25,
        f"Total Tests: {info.tests}",
        f"Tests per Million: {info.tests_per_one_million}",
        f"Cases per Million: {info.cases_per_one_million}",
        f"Deaths per Million: {info.deaths_per_one_million}",
        "-" * 25,
    )
    for line in output:
        print(line)
    if not info.country_info:
        print(f"Affected Countries: {info.affected_countries}")
