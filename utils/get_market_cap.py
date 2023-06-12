import requests


def get_market_cap():
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {
        'symbol': 'BTCUSDT,ETHUSDT,XRPUSDT,LTCUSDT,BCHUSDT,ADAUSDT,DOTUSDT,LINKUSDT,XLMUSDT,DOGEUSDT'}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        market_cap_data = response.json()
        market_cap_values = []
        for item in market_cap_data:
            symbol = item['symbol']
            price = float(item['price'])
            circulating_supply = get_circulating_supply(symbol)
            if circulating_supply:
                market_cap = price * circulating_supply
                market_cap_values.append(market_cap)
        return market_cap_values
    else:
        return None


def get_circulating_supply(symbol):
    url = f'https://api.coingecko.com/api/v3/coins/{symbol.lower()}'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        circulating_supply = float(data['market_data']['circulating_supply'])
        return circulating_supply
    else:
        return None

