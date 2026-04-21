import streamlit as st
import pandas as pd

# Load data
sentiment = pd.read_csv('data/fear_greed_index.csv')
trades = pd.read_csv('data/historical_data.csv')

# Clean
sentiment.columns = sentiment.columns.str.strip().str.lower()
trades.columns = trades.columns.str.strip().str.lower()

sentiment['date'] = pd.to_datetime(sentiment['date'])
trades['timestamp ist'] = pd.to_datetime(trades['timestamp ist'], errors='coerce')
trades = trades.dropna(subset=['timestamp ist'])
trades['date'] = trades['timestamp ist'].dt.floor('D')

# Metrics
daily_pnl = trades.groupby(['date','account'])['closed pnl'].sum().reset_index()
df = daily_pnl.merge(sentiment[['date','classification']], on='date', how='inner')

trades_per_day = trades.groupby('date').size().reset_index(name='num_trades')
merged_trades = trades_per_day.merge(sentiment, on='date')

# UI
st.title("Trader Performance Dashboard")

# PnL chart
st.subheader("Average PnL by Sentiment")
st.bar_chart(df.groupby('classification')['closed pnl'].mean())

# Trades chart
st.subheader("Trading Activity by Sentiment")
st.bar_chart(merged_trades.groupby('classification')['num_trades'].mean())