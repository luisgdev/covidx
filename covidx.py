import requests

url = 'https://corona.lmao.ninja/all'
data = requests.get(url).json()
cases = data['cases']
deaths = data['deaths']
recovered = data['recovered']
deathr = round(deaths/cases*100, 2)
recovr = round(recovered/cases*100, 2)
print('====== COVID19 ======')
print(f'Total cases: {cases}')
print(f'Deaths: {deaths} ({deathr}%)')
print(f'Recovered: {recovered} ({recovr}%)')

