"""
Compute:
    RSI (from scratch)
    Bollinger Bands
    ATR

Return numeric signals for each time point
"""

import pandas as pd
import numpy as np

def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def compute_bollinger_bands(series: pd.Series, window: int = 20, num_std: int = 2):
    sma = series.rolling(window=window).mean()
    std = series.rolling(window=window).std()
    upper_band = sma + (num_std * std)
    lower_band = sma - (num_std * std)
    return sma, upper_band, lower_band

def compute_atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high_low = df['High'] - df['Low']
    high_close = np.abs(df['High'] - df['Close'].shift())
    low_close = np.abs(df['Low'] - df['Close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.rolling(window=period).mean()
    return atr

def compute_indicators(market_data: dict) -> dict:
    """
    Takes raw price data and computes technical indicators (RSI, Bollinger, ATR).
    Returns modified dict of DataFrames with added indicator columns.
    """
    result = {}

    for ticker, df in market_data.items():
        df = df.copy()

        # RSI
        df['RSI'] = compute_rsi(df['Close'])

        # Bollinger Bands
        sma, upper, lower = compute_bollinger_bands(df['Close'])
        df['BB_Mid'] = sma
        df['BB_Upper'] = upper
        df['BB_Lower'] = lower

        # ATR
        df['ATR'] = compute_atr(df)

        result[ticker] = df

    return result
