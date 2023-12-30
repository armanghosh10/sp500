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
warnings.filterwarnings('ignore')


sp500 = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
sp500['Symbol'] = sp500['Symbol'].str.replace('.','-')
symbols = sp500['Symbol'].unique().tolist()
symbols.remove('VLTO')

end_date = '2023-12-05'
start_date = pd.to_datetime(end_date)-pd.DateOffset(365*8)
data = yf.download(tickers=symbols,start=start_date,end=end_date)
data = data.stack()
data.index.names = ['date','ticker']
