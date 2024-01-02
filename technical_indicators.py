def compute_garman_klass_vol(stock_data): 
    stock_data['Garman_Class_Vol'] = ((np.log(stock_data['High'])-np.log(stock_data['Low']))**2)/2-(2*np.log(2)-1)*
    ((np.log(stock_data['Adj Close'])-np.log(stock_data['Open']))**2)
    return stock_data

def compute_rsi(stock_data): 
    stock_data['RSI'] = stock_data.groupby(level=1)['Adj Close'].transform(lambda x: pandas_ta.rsi(close=x, length=20))
    return stock_data

def compute_bbands(stock_data):
    bbands = pandas_ta.bbands(close=np.log1p(stock_data), length=20)
    # The columns will be ['BBL', 'BBM', 'BBU', 'BBB', 'BBP'] by default
    return bbands

def compute_atr(stock_data): 
    atr = pandas_ta.atr(high=stock_data['High'],
                        low=stock_data['Low'],
                        close=stock_data['Close'],
                        length=14)

    return atr.sub(atr.mean()).div(atr.std()) #Returning normalised ATR values

def compute_macd(stock_data):
    macd = pandas_ta.macd(close=stock_data, length=20).iloc[:,0]
    return macd.sub(macd.mean()).div(macd.std())

def compute_dollar_volume(stock_data): 
    stock_data['Dollar Volume'] = (stock_data['Adj Close']*stock_data['Volume'])/1e6
    return stock_data 

def compute_returns(stock_data): 
    outlier_cutoff = 0.005
    lags = [1, 2, 3, 6, 9, 12]
    for lag in lags: 
        stock_data[f'{lag}month_return'] = (stock_data['Adj Close'].pct_change(lag)
                                           .pipe(lambda x: x.clip(lower=x.quantile(outlier_cutoff),
                                            upper=x.quantile(1-outlier_cutoff)))
                                           .add(1).pow(1/lag).sub(1))
    return stock_data
