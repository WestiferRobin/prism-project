"""

Load SPY, BTC, and AAPL

Daily candle data via yfinance or ccxt

Clean, cache, and return DataFrames

"""

def get_market_data(tickers: list) -> dict:
    """
    Fetch and return historical OHLCV data for each ticker.
    Returns a dictionary: { "SPY": DataFrame, "BTC-USD": DataFrame, ... }
    """
    return { "ASDF": tickers }