import datetime

from models.data.stock_data import load_stock_data
from models.data.solar_data import load_solar_data
from models.data.earth_data import fetch_earth_data


def load_physics_data(start_date, end_date):
    solar_data = load_solar_data(start_date, end_date)
    earth_data = fetch_earth_data(start_date, end_date)
    return {
        "solar_data": solar_data,
        "earth_data": earth_data
    }


def load_economy_data(tickers, start_date, end_date):
    stock_data = load_stock_data(tickers, start_date, end_date)
    return {
        "stock_data": stock_data
    }


def load_goose_data(tickers, start_date, end_date):
    """
    Idea: Just get data in the realm of econophysics
    """
    physics_data = load_physics_data(start_date, end_date)
    econ_data = load_economy_data(tickers, start_date, end_date)

    return {
        "physics_data": physics_data,
        "econ_data": econ_data
    }


def run_goose_engine(tickers: list, start_date: datetime.datetime, end_date: datetime.datetime):
    # STEP 1: Load Engine "Goose" Data
    engine_data = load_goose_data(tickers, start_date, end_date)

    """
    TODO:
        1. create ui for all data sources to analysis 
        2. apply the data into a dataset for ML purposes. Try pytorch but consider GPT for the DeepSeek strategy for learning
        3. Implement other steps below. physic_data + econ_data = action to invest or trade
    
    """

    ## TODO FIX THIS EVERY STEP
    # # STEP 2: Compute Indicators
    # indicator_data = compute_indicators(engine_data)
    #
    # # STEP 3: Generate Buy/Sell/Hold Signals
    # signal_data = generate_signals(indicator_data)
    #
    # # STEP 4: Simulate Trades and Log Them
    # execute_paper_trades(signal_data, indicator_data)
    #
    # # STEP 5: Visualize the root chart for len(tickers) stocks
    # run_goose_dashboard(tickers, indicator_data)
