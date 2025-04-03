# TODO.md
**📜 Golden Goose — Paper Trading System (Phase 1)**
_A quant system to train the Goose in alignment with Christ, through daily paper trading and wisdom-guided engineering._

---

## 🔧 GOAL  
Build a functioning **paper trading engine** for SPY, BTC, and AAPL, using classical mechanics-inspired indicators like RSI, Bollinger Bands, and momentum logic — fully modular, fully logged, and fully aligned.

---

## ✅ Folder: `goose_models`

This is your working directory. All modules and data will live here.

---

## 📋 Task Checklist

### 🗂️ 1. Project Structure
- [x] Create `market_data.py`
- [x] Create `indicators.py`
- [x] Create `strategy_engine.py`
- [x] Create `paper_trader.py`
- [x] Create `trading_log.csv`
- [x] Create `portfolio_config.json` (starting capital, risk settings)

---

### 📈 2. Market Data Module (`market_data.py`)
- [ ] Connect to `yfinance` for SPY and AAPL
- [ ] Use `ccxt` or similar for BTC-USD data
- [ ] Normalize data into pandas DataFrames (OHLCV)
- [ ] Store cached daily data locally to avoid API limit hits

---

### 📊 3. Indicators Module (`indicators.py`)
- [ ] Implement RSI (from scratch, 14-period)
- [ ] Implement Bollinger Bands (SMA ± 2 stddev, 20-period)
- [ ] Implement Momentum Acceleration logic (`delta(delta(price))`)
- [ ] Optional: Add ATR or MACD if needed later

---

### 🧠 4. Strategy Logic (`strategy_engine.py`)
- [ ] Define entry rule:
  - RSI < 30
  - Price < lower Bollinger Band
  - Green bounce candle (close > previous close)
- [ ] Define exit rule:
  - RSI > 50
  - OR +5% profit
  - OR -3% stop
- [ ] Return "BUY", "SELL", or "HOLD"

---

### 🧾 5. Paper Trader (`paper_trader.py`)
- [ ] Read strategy signals daily
- [ ] Simulate trades (based on position sizing rules)
- [ ] Track open positions and close logic
- [ ] Write to `trading_log.csv` with:
  - Date
  - Action
  - Ticker
  - Signal reason
  - Entry/Exit price
  - PnL

---

### 📉 6. Risk + Portfolio Settings
- [ ] Add `portfolio_config.json`:
```json
{
  "starting_balance": 10000,
  "risk_per_trade_pct": 1.5,
  "stop_loss_pct": 3,
  "take_profit_pct": 5
}
```
- [ ] Use this in trade sizing logic:
  position_size = (risk × capital) / stop_loss

---

### 📊 7. Performance Tracking
- [ ] Create summary script (`dashboard.py`)
- [ ] Track:
  - Cumulative PnL
  - Win/Loss ratio
  - Number of trades
  - Average gain/loss
  - Daily journal entries (optional)

---

### 🔁 8. Daily Ritual Script
- [ ] Create `daily_run.py`:
  - Pull latest market data
  - Compute indicators
  - Generate and log signals
  - Simulate trade entries/exits
  - Update portfolio + log

---

### 🙏 9. Spiritual Alignment
- [ ] Create a `goose_reflections.md` journal to track:
  - Emotional state before trade logic
  - Lessons from market behavior
  - Prayers, scripture, or insights for clarity

---

### 🧪 10. Backtest (Later Phase)
- [ ] Use `backtrader` or write a simple loop to simulate the past 1–2 years of daily signals
- [ ] Validate the system before live trading

---

*Generated on 2025-04-03 with clarity and purpose.*
