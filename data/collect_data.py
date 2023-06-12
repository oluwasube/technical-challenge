import requests
import csv
import sys
import os

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
        headers = ["Open_Time", "Open", "High", "Low", "Close", "Volume", "Close Time", "Quote Asset Volume",
                   "Number_of_Trades", "Taker_buy_volume", "Taker_Buy_Quote_Volume", "Ignore"]

        directory = "data"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = f"{symbol}_{interval}.csv"

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        print(f"Data collected and saved for {symbol} at {interval}")
    else:
        print("Failed to fetch data from the Binance API.")


if __name__ == "__main__":
    symbol = input("Enter the symbol (e.g., BTCUSDT): ")
    interval = input("Enter the interval (e.g., 4h): ")
    collect_data(symbol, interval)
