####### Sourcing Index data for project ########

#---------------------------------------- 1) Nifty 50 Index -----------------------------
# Manual Download of data: 35 years, API: 18 years

# Manually .csv can be downloaded from https://www.niftyindices.com/reports/historical-data

# Code to source Nifty 50 Index Data from Yahoo Finance API
# https://ranaroussi.github.io/yfinance/
# https://pypi.org/project/yfinance/
# Full API referrence - https://ranaroussi.github.io/yfinance/reference/index.html

# pip install yfinance

import yfinance as yf
from pprint import pprint
import pandas as pd


# Nifty 50 ticker symbol
nifty = yf.Ticker("^NSEI")

# Get historical data (default 1 month if not specified) - Note only data from 2007 is available
df = nifty.history(period="30y")  # You can change to "5d", "1mo", "1y", etc.

# Save to Excel
df.to_csv("nifty50_history.csv")

# Show first few rows
print(df.head())


#---------------------------------------- 1) BAX Bahrain's Index -----------------------------

# Manually .csv for 15 year data can be downloaded from https://www.investing.com/indices/bax-historical-data

# API does not have data/symbol for BAX


#---------------------------------------- 1) USA's S&P 500 Index -----------------------------

# Manually .csv for 16 year data can be downloaded from https://www.investing.com/indices/us-spx-500-historical-data

# Code to source S&P 500 Index Data from Yahoo Finance API - 30 year data

# Nifty 50 ticker symbol
sp500 = yf.Ticker("^GSPC")

# Get historical data (default 1 month if not specified) - Note only data from 2007 is available
df_2 = sp500.history(period="30y")  # You can change to "5d", "1mo", "1y", etc.

# Save to Excel
df_2.to_csv("sp500_history.csv")

# Show first few rows
print(df.head())