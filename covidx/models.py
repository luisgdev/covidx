"""Models"""

from typing import Optional

from pydantic import BaseModel, Field


class CovidApi:
    """
    API endpoints.
    """

    _BASE_URL: str = "https://disease.sh/v3/covid-19"
    ALL_: str = f"{_BASE_URL}/all"
    COUNTRIES_: str = f"{_BASE_URL}/countries/"


class Global(BaseModel):
    """Global data"""

    updated: int
    cases: int
    today_cases: int = Field(..., alias="todayCases")
    today_deaths: int = Field(..., alias="todayDeaths")
    deaths: int
    recovered: int
    today_recovered: int = Field(..., alias="todayRecovered")
    active: int
    critical: int
    cases_per_one_million: float = Field(..., alias="casesPerOneMillion")
    deaths_per_one_million: float = Field(..., alias="deathsPerOneMillion")
    tests: int
    tests_per_one_million: float = Field(..., alias="testsPerOneMillion")
    population: int
    one_case_per_people: int = Field(..., alias="oneCasePerPeople")
    one_death_per_people: int = Field(..., alias="oneDeathPerPeople")
    one_test_per_people: int = Field(..., alias="oneTestPerPeople")
    active_per_one_million: float = Field(..., alias="activePerOneMillion")
    recovered_per_one_million: float = Field(..., alias="recoveredPerOneMillion")
    critical_per_one_million: float = Field(..., alias="criticalPerOneMillion")
    affected_countries: Optional[int] = Field(None, alias="affectedCountries")
