from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import pandas_ta
import warnings

#Calculating all the technical indicators for S&P500 Stocks 
compute_garman_klass_vol(data)
compute_rsi(data)
# Initialize lists to store Bollinger Bands
bb_lows = []
bb_mids = []
bb_highs = []

# Calculate Bollinger Bands for each group
for name, group in df.groupby(level='ticker'):
    bbands = compute_bbands(group['Adj_Close'])
    # Assuming 'bbands' DataFrame has the same index as 'group'
    bb_lows.extend(bbands['BBL_20_2.0'])
    bb_mids.extend(bbands['BBM_20_2.0'])
    bb_highs.extend(bbands['BBU_20_2.0'])

# Assign the results back to the DataFrame
data['bb_low'] = bb_lows
data['bb_mid'] = bb_mids
data['bb_high'] = bb_highs
