from src.models.goose_models.engine_models.model import run_goose_engine


def run_golden_goose():
    test_tickers = ["SPY", "BTC-USD", "AAPL"]
    run_goose_engine(test_tickers)
