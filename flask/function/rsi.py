import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from .data import company
now = datetime.now()
aend=now-timedelta(days=1)
astart=aend-timedelta(days=20)

start_date = astart.strftime('%Y-%m-%d')
end_date = aend.strftime('%Y-%m-%d')

def main():
    low_rsi_stocks = []
    for i in company:
        data=yf.download(i,start=start_date,end=end_date,interval="1d")
        data['RSI'] = calculate_rsi(i,data, 14)
        if data['RSI'].isna().all():
            print(f"RSI cannot be calculated for {i}")
            continue
        last_rsi = data['RSI'].iloc[-1]
        if last_rsi <= 35:
            low_rsi_stocks.append((i, last_rsi))
    return low_rsi_stocks

def calculate_rsi(name,data, window):
    ticker=name
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))           
    return rsi
if __name__ == "__main__":
    main()


