"""
Simulates trades

Logs:
    Entry/exit time
    Position size
    PnL
    Reason for entry

Stores in trading_log.json or .csv
"""

import csv
import os
from datetime import datetime

def execute_paper_trades(signals: dict, full_data: dict):
    LOG_FILE = "trading_log.csv"

    # Initialize log file with headers if not present
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Ticker", "Action", "Price", "PositionSize", "PnL", "Reason"])
    """
    Simulates trades based on signals.
    Updates trade log and returns simulated portfolio changes.
    """
    for ticker, signal in signals.items():
        df = full_data[ticker].copy()
        latest = df.iloc[-1]
        date = latest.name.strftime('%Y-%m-%d')
        price = latest['Close']
        reason = "RSI < 30, Price < BB_Lower, Bounce"
        position_size = 100  # For now, static size
        pnl = 0  # Placeholder

        if signal == "BUY":
            action = "BUY"
        elif signal == "SELL":
            action = "SELL"
        else:
            continue

        with open(LOG_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, ticker, action, price, position_size, pnl, reason])