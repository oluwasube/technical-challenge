# Candlestick and Pie Chart Application
This is a Python application that uses Flask and Dash frameworks to create a web-based dashboard with two charts: a candlestick chart and a pie chart. The candlestick chart displays the historical price data of a cryptocurrency, while the pie chart shows the market capitalization of various cryptocurrencies.

## Prerequisites
- Python 3.x
- Flask
- Dash
- Plotly
- pandas

## Installation

To install and run this Python application, follow the steps below:

1. Clone the repository download the code files to your local machine.
2. Open your terminal and navigate to the directory where the cloned application is located.
3. Create a virtual environment using the following command:
   - For Linux or Windows Git Bash Terminal: `python3 -m venv env`
4. Activate the virtual environment with the command below:
   - For Linux or Windows Git Bash Terminal: `source env/bin/activate`
5. Install the required dependencies by running the following command:`pip install -r requirements.txt`.
6. run the application using the following command:`python3 app.py`
7. Once the application is running, open a web browser and go to `http://localhost:8050` to access the dashboard.

**Note:** Make sure you have Python and pip installed on your machine before proceeding with the above steps.

# Binance Data Collector

1. Open a terminal or command prompt and navigate to the directory `data` where the script is located.

2. Run the script by executing the following command:`python3 collect_data.py`

3. Follow the prompts to enter the symbol and interval.

4. The script will connect to the Binance API and fetch the historical price data.

5. The data will be saved to a CSV file in the "data" directory with the filename `{symbol}_{interval}.csv`.

6. Once the process is complete, the script will print a message indicating that the data has been collected and saved.

## Code Explanation

- The code starts by importing the necessary modules and packages.
- It creates a Flask app and a Dash app.
- The `data` directory is searched for CSV files, and the first file found is read into a Pandas DataFrame.
- The layout of the web page is defined using HTML and Dash components. The candlestick chart and pie chart are added to the layout.
- The candlestick chart is generated using the Plotly library, with the historical price data from the CSV file.
- The pie chart is also created using Plotly, with predefined labels and values representing the market capitalization of different cryptocurrencies.
- Finally, the Flask server is started, and the application is run.
