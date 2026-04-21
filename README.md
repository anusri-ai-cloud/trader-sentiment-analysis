# Trader Performance vs Market Sentiment

## Overview
This project analyzes how market sentiment (Fear vs Greed) affects trader behavior and performance.

## Features
- Data cleaning and preprocessing
- Daily PnL analysis
- Win rate, trade frequency, and trade size
- Long/short ratio
- Trader segmentation
- Clustering of traders
- Simple predictive model
- Streamlit dashboard

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run notebook
Open analysis.ipynb and run all cells

### Run dashboard
streamlit run app.py

## Insights
- Higher volatility during Greed periods
- Increased trading activity during Fear
- Larger trades increase risk
- Consistent traders perform better

## Strategy
- Reduce risk during Fear
- Maintain discipline during Greed
- Focus on consistent trading behavior

## Data

Due to file size limitations, datasets are not included in this repository.

You can download them from:

- Fear & Greed Index: [link]
- Historical Data: [link]

Place them inside a `data/` folder before running the code.
