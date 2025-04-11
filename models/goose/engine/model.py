import datetime

from models.data.market_data import load_market_data
from models.data.solar_data import load_solar_data
from models.data.weather_data import load_weather_data


def load_physics_data(start_date, end_date):
    load_solar_data(start_date, end_date)
    load_weather_data(start_date, end_date)

def load_economy_data(tickers, start_date, end_date):
    load_market_data(tickers, start_date, end_date)

def load_goose_data(tickers, start_date, end_date):
    load_physics_data(start_date, end_date)
    load_economy_data(tickers, start_date, end_date)


def run_goose_engine(tickers: list, start_date: datetime.datetime, end_date: datetime.datetime):
    # STEP 1: Load Market Data
    load_goose_data(tickers, start_date, end_date)

    # STEP 1: Load Market Data
    # market_data = get_market_data(tickers)

    ## TODO FIX THIS EVERY STEP
    # # STEP 2: Compute Indicators
    # data_with_indicators = compute_indicators(market_data)
    #
    # # STEP 3: Generate Buy/Sell/Hold Signals
    # signals = generate_signals(data_with_indicators)
    #
    # # STEP 4: Simulate Trades and Log Them
    # execute_paper_trades(signals, data_with_indicators)
    #
    # # STEP 5: Visualize the root chart for len(tickers) stocks
    # plot_stock_chart(tickers, data_with_indicators)
