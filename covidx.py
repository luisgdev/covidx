import sys
import requests

# Source
url = 'https://corona.lmao.ninja/'

# Set url endpoint
if len(sys.argv) == 1:
    print('WORLD')
    url += 'all'
else:
    country = sys.argv[1]
    print(country.upper())
    url += f'countries/{country}'

# Request data
data = requests.get(url).json()

# Process data
cases = data['cases']
deaths = data['deaths']
recovered = data['recovered']
deathr = round(deaths/cases*100, 2)
recovr = round(recovered/cases*100, 2)

print('======== COVID19 ========')
print(f'Total cases: {cases}')
print(f'Deaths: {deaths} ({deathr}%)')
print(f'Recovered: {recovered} ({recovr}%)')
print('=========================')
