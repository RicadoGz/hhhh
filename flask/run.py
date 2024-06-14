#run.py
from flask import Flask, request, render_template
import yfinance as yf
import os
import pandas as pd
import mplfinance as mpf
import matplotlib
matplotlib.use('Agg') 
from function.rsi import main as rsi_main
from tempfile import NamedTemporaryFile


app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/ability')
def ability():
    return render_template('self.html')

@app.route('/search', methods=['POST'])
def search():
    stock = request.form.get('stock')
    ticker = yf.Ticker(stock)
    stock_data = yf.download(stock, start="2022-01-01", end="2023-01-01")
    selected_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]




    csv_file = f'{stock}.csv'
    csv_path = os.path.join(app.static_folder, csv_file)
    img_filename = f'{stock}.png'
    img_path = os.path.join(app.static_folder, img_filename)

    if os.path.exists(csv_path):
        selected_data.to_csv(csv_path, mode='a', header=False)
    else:
        selected_data.to_csv(csv_path)
    generate_plot(selected_data, stock, img_path)
    return render_template('mar.html', stock=stock, img_path=img_filename)
    


    
def generate_plot(data, stock, path):
    mpf.plot(data, type='candle', volume=True, style='charles', 
                title=f'{stock} K线图', ylabel='价格', ylabel_lower='交易量', 
                mav=(20, 50), savefig=path)
@app.route('/mar')
def mar():
    return render_template('mar.html')
@app.route('/rsi',methods=['GET', 'POST'])
def rsi():
    low_rsi_stocks = rsi_main()
    return render_template('rsi.html',first=low_rsi_stocks)

if __name__ == '__main__':
    app.run(debug=True)
