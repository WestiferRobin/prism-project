"""

Daily update:
    Current signals
    Open positions
    Performance chart vs. $6K/month goal
    Win rate and accuracy

"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_ticker_chart(ticker: str, df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Close Price', linewidth=1.5)
    plt.plot(df.index, df['BB_Upper'], label='BB Upper', linestyle='--', alpha=0.6)
    plt.plot(df.index, df['BB_Lower'], label='BB Lower', linestyle='--', alpha=0.6)
    plt.plot(df.index, df['RSI'], label='RSI', linestyle=':', alpha=0.7)

    plt.title(f"{ticker} - Price, Bollinger Bands & RSI")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()


def run_goose_dashboard(tickers: list, data_with_indicators):
    for ticker in tickers:
        plot_ticker_chart(ticker, data_with_indicators[ticker])

