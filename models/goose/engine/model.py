import datetime

from models.goose.goose_ui.solar_system_ui import run_solar_system_ui


def run_goose_engine(tickers: list, start_date: datetime.datetime=None, end_date: datetime.datetime=None):
    if end_date is None:
        end_date = datetime.datetime.now(datetime.UTC)

    if start_date is None:
        start_date = datetime.datetime.combine(
            end_date.date().replace(year=end_date.year - 5),
            datetime.time.min,
            tzinfo=datetime.UTC
        )

    # STEP 2: Load Sudo Data => cosmos from sun to earth, and it's perspective with the weather
    # solar_data = get_planet_data(start_date, end_date)
    run_solar_system_ui(start_date, end_date)

    print(f"predicting stonks for {tickers} with cosmos and weather data on markets")
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
