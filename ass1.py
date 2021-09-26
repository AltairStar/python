from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
cin = int(input())

arr = cg.get_coins_markets('usd')

def my_function(arr):
    return arr.get('current_price')

arr = sorted(arr,key = my_function,reverse=True)
for i in range(cin):
    print("{0} {1}".format(arr[i].get('current_price'),arr[i].get('id')))





