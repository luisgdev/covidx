"""Models"""

from typing import Dict, Optional

from pydantic import BaseModel


class API:
    """
    API endpoints.
    """

    _base_url: str = "https://disease.sh/v3/covid-19"
    all_: str = f"{_base_url}/all"
    country: str = f"{_base_url}/countries/"


class CountryInfo(BaseModel):
    """Country info"""

    _id: int
    iso2: str
    iso3: str
    lat: float
    long_: float
    flag: str

    class Config:
        """Parse properties"""

        fields: Dict[str, str] = {
            "long_": "long",
        }


class Global(BaseModel):
    """Global data"""

    updated: int
    cases: int
    today_cases: int
    today_deaths: int
    deaths: int
    recovered: int
    today_recovered: int
    active: int
    critical: int
    cases_per_one_million: float
    deaths_per_one_million: float
    tests: int
    tests_per_one_million: float
    population: int
    one_case_per_people: int
    one_death_per_people: int
    one_test_per_people: int
    active_per_one_million: float
    recovered_per_one_million: float
    critical_per_one_million: float
    affected_countries: Optional[int]
    country_info: Optional[CountryInfo]
    continent: Optional[str]

    class Config:
        """Parse properties"""

        fields: Dict[str, str] = {
            "today_cases": "todayCases",
            "today_deaths": "todayDeaths",
            "today_recovered": "todayRecovered",
            "cases_per_one_million": "casesPerOneMillion",
            "deaths_per_one_million": "deathsPerOneMillion",
            "tests_per_one_million": "testsPerOneMillion",
            "one_case_per_people": "oneCasePerPeople",
            "one_death_per_people": "oneDeathPerPeople",
            "one_test_per_people": "oneTestPerPeople",
            "active_per_one_million": "activePerOneMillion",
            "recovered_per_one_million": "recoveredPerOneMillion",
            "critical_per_one_million": "criticalPerOneMillion",
            "affected_countries": "affectedCountries",
            "country_info": "countryInfo",
        }
