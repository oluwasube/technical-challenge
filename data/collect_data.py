import requests
import csv
import os

import time
from datetime import datetime


def collect_data(symbol, interval):
    base_url = "https://api.binance.com/api/v3/klines"

    # start_time = int(time.time() * 1000) - \
    #     (get_intervals(interval) * 1000)

    params = {
        "symbol": symbol,
        "interval": interval,
        # "startTime": start_time,
        "limit": 1000  # Maximum limit per request
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

        filename = f"{directory}/{symbol}_{interval}.csv"

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        print(f"Data collected and saved for {symbol} at {interval}")
    else:
        print("Failed to fetch data from the Binance API.")


if __name__ == "__main__":
    symbol = "BTCUSDT"
    interval = "4h"
    collect_data(symbol, interval)
