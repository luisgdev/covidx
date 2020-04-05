import requests

url = 'https://corona.lmao.ninja/all'
data = requests.get(url).json()
cases = data['cases']
print(cases)
