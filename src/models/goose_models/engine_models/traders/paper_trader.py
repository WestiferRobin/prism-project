"""

Simulates trades

Logs:
    Entry/exit time
    Position size
    PnL
    Reason for entry

Stores in trading_log.json or .csv

"""

def execute_paper_trades(signals: dict, full_data: dict):
    """
    Simulates trades based on signals.
    Updates trade log and returns simulated portfolio changes.
    """

# TODO: Refactor for real trading