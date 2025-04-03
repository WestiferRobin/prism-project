from src.models.goose_models.dashboard import plot_stock_chart
from src.models.goose_models.engine_models.indicators import compute_indicators
from src.models.goose_models.engine_models.market_data import get_market_data
from src.models.goose_models.engine_models.strategy_engine import generate_signals
from src.models.goose_models.engine_models.traders.paper_trader import execute_paper_trades


def run_goose_engine(tickers: list):
    # STEP 1: Load Market Data
    market_data = get_market_data(tickers)

    # STEP 2: Compute Indicators
    data_with_indicators = compute_indicators(market_data)

    # STEP 3: Generate Buy/Sell/Hold Signals
    signals = generate_signals(data_with_indicators)

    # STEP 4: Simulate Trades and Log Them
    execute_paper_trades(signals, data_with_indicators)

    # STEP 5: Visualize the root chart for len(tickers) stocks
    plot_stock_chart(tickers, data_with_indicators)