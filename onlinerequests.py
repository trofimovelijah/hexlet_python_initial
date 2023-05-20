import requests

API_KEY = 'zfccPwlWsuPd5A1fwp1NGoHKTMDqoiiEBEZqxeQf'

HOST = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies=EUR%2CUSD%2CRUB%2CGBP'

response = requests.get(HOST)

print(response.json()['data'])