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
