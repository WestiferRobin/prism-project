import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

from configs.goose_config import DATA_CACHE

def load_market_data(tickers: list, start_date: datetime, end_date: datetime) -> dict:
    data_dict = {}

    data_path = f"{DATA_CACHE}/{end_date}"
    os.makedirs(data_path, exist_ok=True)

    for ticker in tickers:
        cache_file = os.path.join(data_path, f"{ticker}_data.csv")

        if os.path.exists(cache_file):
            df = pd.read_csv(cache_file, index_col=0, parse_dates=True)
            last_cached = pd.to_datetime(df.index[-1])
            if last_cached >= pd.to_datetime(end_date - timedelta(days=1)):
                data_dict[ticker] = df
                continue

        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        df.dropna(inplace=True)
        df.to_csv(cache_file)
        data_dict[ticker] = df

    return data_dict
