import sys
import requests

# Source
url = 'https://corona.lmao.ninja/v2/'

# Set url endpoint
if len(sys.argv) == 1:
    print('WORLD')
    url += 'all'
else:
    country = sys.argv[1]
    print(f'==== COVID19 IN {country.upper()} ====')
    url += f'countries/{country}'

# Request data
data = requests.get(url).json()

# Process data
cases = data['cases']
deaths = data['deaths']
recovered = data['recovered']
deathr = round(deaths/cases*100, 2)
recovr = round(recovered/cases*100, 2)
tests = data['tests']
todayCases = data['todayCases']
todayDeaths = data['todayDeaths']
active = data['active']
critical = data['critical']
casesPerOneMillion = data['casesPerOneMillion']
deathsPerOneMillion = data['deathsPerOneMillion']
testsPerOneMillion = data['testsPerOneMillion']
if len(sys.argv) == 1:
    affectedCountries = data['affectedCountries']
    print('======== COVID19 ========')
print(f'Total Cases: {cases}')
print(f'Deaths: {deaths} ({deathr}%)')
print(f'Recovered: {recovered} ({recovr}%)')
print('-------------------------')
print(f'Today Cases: {todayCases}')
print(f'Today Deaths: {todayDeaths}')
print('-------------------------')
print(f'Active Cases: {active}')
print(f'Critical Cases: {critical}')
print('-------------------------')
print(f'Total Tests: {tests}')
print(f'Tests per Million: {testsPerOneMillion}')
print(f'Cases per Million: {casesPerOneMillion}')
print(f'Deaths per Million: {deathsPerOneMillion}')
print('-------------------------')
if len(sys.argv) == 1:
    print(f'Affected Countries: {affectedCountries}')
    print('=========================')
