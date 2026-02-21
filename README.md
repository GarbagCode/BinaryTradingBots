# 📈 Binary Trading Bot

A machine learning-based trading bot that predicts binary price movements (**up/down**) for Bitcoin using XGBoost.  
The bot analyzes historical **BTC/USD** price data with technical indicators to forecast the next price direction.

---

## 🚀 Features

- 📊 Technical indicators:
  - SMA (Simple Moving Average)
  - RSI (Relative Strength Index)
  - ATR (Average True Range)
  - VWAP (Volume Weighted Average Price)
  - MACD (Moving Average Convergence Divergence)
  - Support & Resistance levels
- 🤖 XGBoost classifier for binary prediction (price up vs. down)

---

## 🛠 Tech Stack

- **Python**
- **Pandas**
- **XGBoost**
- **pandas-ta** (Technical Analysis library)
- Historical Bitcoin price data (OHLCV format)

---

## 📊 Model Objective

The model predicts whether the next candle's closing price will be:

- 📈 **Up (1)**
- 📉 **Down (0)**

This is a classification problem rather than regression — focused purely on direction, not magnitude.

---

## ⚙️ How It Works

1. Load historical OHLCV Bitcoin data.
3. Generate technical indicators.
4. Engineer features for supervised learning.
5. Train XGBoost classifier.
6. Output probability-based directional prediction.

---

## 📌 Future Improvements

- Hyperparameter tuning
- Cross-validation with walk-forward testing
- Live API integration
- Risk management system
- Trade execution automation

---

## ⚠️ Disclaimer

This project is for educational purposes only.  
Cryptocurrency trading involves substantial risk and is not financial advice.

## ❤️ Support the Project

If you find this useful and want to support continued development:
👉 https://www.patreon.com/c/GarbageCode
