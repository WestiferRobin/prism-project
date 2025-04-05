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
    signals = {}

    for ticker, df in data_with_indicators.items():
        df = df.copy()

        if len(df) < 2:
            signals[ticker] = "HOLD"
            continue

        latest = df.iloc[-1]
        prev = df.iloc[-2]

        rsi = latest['RSI']
        close = latest['Close']
        bb_lower = latest['BB_Lower']
        prev_close = prev['Close']

        # Strategy conditions
        if rsi < 30 and bb_lower > close > prev_close:
            signals[ticker] = "BUY"
        elif close < prev_close and rsi > 70:
            signals[ticker] = "SELL"
        else:
            signals[ticker] = "HOLD"

    return signals
