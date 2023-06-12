import requests
import csv
import time


def collect_data(symbol, interval):
    base_url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": 1000
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:

        data = response.json()

        # Format data and save to CSV
        headers = ["Open Time", "Open", "High", "Low", "Close", "Volume", "Close Time", "Quote Asset Volume",
                   "Number_of_Trades", "Taker_buy_volume", "Taker_Buy_Quote_Volume", "Ignore"]

        filename = f"{symbol}_{interval}.csv"

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        print(f"Data collected and saved for {symbol} at {interval} interval.")
    else:
        print("Failed to fetch data from the Binance API.")


# symbol = "BTCUSDT"
# interval = "1h"
# collect_data(symbol, interval)
