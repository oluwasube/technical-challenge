from flask import Flask, render_template
import csv
import plotly.graph_objects as go

app = Flask(__name__, template_folder='templates')


@app.route("/")
def display_data():
    # Read candlestick data from CSV
    filename = "BTCUSDT_1h.csv"

    with open(filename, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    open_time = [row[0] for row in data[1:]]
    close = [float(row[4]) for row in data[1:]]
    high = [float(row[2]) for row in data[1:]]
    low = [float(row[3]) for row in data[1:]]
    Open = [float(row[1]) for row in data[1:]]

    # Create candlestick chart
    candlestick_chart = go.Candlestick(
        x=open_time, open=Open, high=high, low=low, close=close
    )

    # Create pie chart
    symbols = ["BTC", "ETH", "XRP", "LTC", "BCH",
               "ADA", "DOT", "LINK", "XLM", "DOGE"]
    market_caps = [1000, 800, 600, 500, 400, 300, 200, 150, 100, 50]

    pie_chart = go.Pie(labels=symbols, values=market_caps)

    layout = go.Layout(
        title='Candlestick Data and Market Caps',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Price'),
        showlegend=False
    )

    fig = go.Figure(data=(candlestick_chart, pie_chart), layout=layout)

    # Convert the figure to JSON for rendering
    plot_div = fig.to_json()

    return render_template('index.html', plot_div=plot_div)



if __name__ == "__main__":
    app.run(debug=True)
