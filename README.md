# Pycoingecko usage
Language used:python\
Version:3.9
Writing in terminal:
```bash
pip install pycoingecko
```
For using pycoingecko API
```bash
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```
Inputing the number of cryptocurrencies
```bash
cin = int(input())
```
Creating list which will store all supported coins price, market cap, volume, and market related data, to solve the problem\
"Too Many Requests for url: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd" 
```bash
arr = cg.get_coins_markets('usd')
```
Sorting list by his 'current_name'
```bash
def my_function(arr):
    return arr.get('current_price')
arr = sorted(arr,key = my_function,reverse=True)
```
Creating the loop for output the N number of cryptocurrencies from sorted list, which will output their name and price
```bash
for i in range(cin):
    print("{0} {1}".format(arr[i].get('current_price'),arr[i].get('id')))
```
