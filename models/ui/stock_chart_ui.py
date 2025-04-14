import yfinance as yf
import matplotlib.pyplot as plt
import math

# === Configurations ===
TICKER = "AAPL"
START_DATE = "1950-01-01"
END_DATE = "2024-01-01"


def load_yfinance_data(ticker, start_date, end_date):
    yfinance_intervals = {
        "d": (1, 5),
        "wk": (1,),
        "mo": (1, 3)
    }
    total_plots = sum(len(lengths) for lengths in yfinance_intervals.values())
    cols = 4
    rows = math.ceil(total_plots / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))
    fig.suptitle(f"{ticker} Stock Price Overview by Interval", fontsize=20)

    axes = axes.flatten() if total_plots > 1 else [axes]
    plot_idx = 0
    for mode, lengths in yfinance_intervals.items():
        for length in lengths:
            interval_str = f"{length}{mode}"
            data = yf.download(ticker, start=start_date, end=end_date, interval=interval_str)
            ax = axes[plot_idx]

            if data is not None:
                data['Close'].plot(ax=ax, title=f"Interval: {interval_str}", grid=True)
                ax.set_xlabel("Date")
                ax.set_ylabel("Price ($)")
            else:
                ax.set_visible(False)

            plot_idx += 1

    # Hide any remaining unused subplots
    for i in range(plot_idx, len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


def load_other_data(ticker, start_date, end_date):
    other_intervals = {
        "m": (2, 5, 15, 30, 90),  # Minute-based: Only available for last 60 days
        "h": (1, 4),              # Hour-based: Up to 730 days
    }
    total_plots = sum(len(lengths) for lengths in other_intervals.values())
    cols = 4
    rows = math.ceil(total_plots / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))
    fig.suptitle(f"{ticker} Stock Price Overview by Interval", fontsize=20)

    axes = axes.flatten() if total_plots > 1 else [axes]
    plot_idx = 0
    for mode, lengths in other_intervals.items():
        for length in lengths:
            interval_str = f"{length}{mode}"
            data = yf.download(ticker, start=start_date, end=end_date, interval=interval_str)
            ax = axes[plot_idx]

            if data is not None:
                data['Close'].plot(ax=ax, title=f"Interval: {interval_str}", grid=True)
                ax.set_xlabel("Date")
                ax.set_ylabel("Price ($)")
            else:
                ax.set_visible(False)

            plot_idx += 1

    # Hide any remaining unused subplots
    for i in range(plot_idx, len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


# === Main Runner ===
if __name__ == "__main__":
    # load_yfinance_data(TICKER, START_DATE, END_DATE)
    load_other_data(TICKER, START_DATE, END_DATE)
