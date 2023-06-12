import os
from flask import Flask
from dash import Dash, dcc, html
import plotly.graph_objects as go
import pandas as pd

# Create Flask app
server = Flask(__name__)
app = Dash(__name__, server=server)

directory = "data"
files = os.listdir(directory)
csv_files = [file for file in files if file.endswith('.csv')]

if len(csv_files) > 0:
    filename = csv_files[0]
    data_path = f"{directory}/{filename}"
    data = pd.read_csv(data_path)

    # Extract the part of the CSV filename before the first "_"
    csv_filename = filename.split("_", 1)[0]
else:
    data = pd.DataFrame()
    csv_filename = "No CSV file available"


app.layout = html.Div([
    html.H1('Candlestick Chart'),
    dcc.Graph(
        id='candlestick-chart',
        figure={
            'data': [
                go.Candlestick(
                    x=pd.to_datetime(data['Open_Time'], unit='ms'),
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close']
                )
            ],
            'layout': go.Layout(
                title=f"{csv_filename} Candlestick Chart",
                xaxis=dict(title='Date'),
                yaxis=dict(title='Price')
            )
        }
    ),
    html.H1('Market Cap Pie Chart'),
    dcc.Graph(
        id='market-cap-pie-chart',
        figure={
            'data': [
                go.Pie(
                    labels=["BTC", "ETH", "XRP", "LTC", "BCH",
                            "ADA", "DOT", "LINK", "XLM", "DOGE"],
                    values=[1000, 800, 600, 500, 400, 300, 200, 150, 100, 50]
                )
            ],
            'layout': go.Layout(
                title='Market Cap',
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
