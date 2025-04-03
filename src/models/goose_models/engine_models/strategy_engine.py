"""

Logic:
    RSI < 30
    Price below lower Bollinger
    Momentum bounce candle

Returns: "BUY", "HOLD", or "SELL"

"""

def generate_signals(data_with_indicators: dict) -> dict:
    """
    Uses strategy logic to return a dictionary of signals.
    Example: { "SPY": "BUY", "BTC-USD": "HOLD", "AAPL": "SELL" }
    """
    return data_with_indicators
