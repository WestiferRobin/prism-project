from models.goose.engine.market_data import get_market_data


def run_goose_engine(tickers: list):
    # STEP 1: Load Market Data
    market_data = get_market_data(tickers)

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