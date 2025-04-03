"""

Compute:
    RSI (from scratch)
    Bollinger Bands
    ATR

Return numeric signals for each time point

"""

def compute_indicators(market_data: dict) -> dict:
    """
    Takes raw price data and computes technical indicators (RSI, Bollinger, etc.)
    Returns modified dict of DataFrames with added indicator columns.
    """
    return market_data