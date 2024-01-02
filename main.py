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
data['BB_Low'] = bb_lows
data['BB_Mid'] = bb_mids
data['BB_High'] = bb_highs

data['ATR'] = data.groupby(level=1, group_keys=False).apply(compute_atr)
data['MACD'] = data.groupby(level=1, group_keys=False)['Adj Close'].apply(compute_macd)
compute_dollar_volume(data)

cols_list = []
for columns in data.columns.unique(0).tolist():
    if columns not in ['Dollar Volume','Volume','Open','High','Low','Close']:
        cols_list.append(columns)
data = pd.concat([data.unstack('ticker')['Dollar Volume'].resample('M').mean().stack('ticker').to_frame('Dollar Volume'),
           data.unstack()[cols_list].resample('M').last().stack('ticker')],axis=1).dropna()

data['Dollar Volume'] = data['Dollar Volume'].unstack('ticker').rolling(5*12).mean().stack()
data['Dollar Volume Rank'] = (data.groupby('date')['Dollar Volume'].rank(ascending=False))
data = data[data['Dollar Volume Rank']<150].drop(['Dollar Volume', 'Dollar Volume Rank'], axis=1)
