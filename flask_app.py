
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
from datetime import date
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Rom Phirunronnakon!'

@app.route('/today')
def hello_today():
    return str(date.today())

@app.route('/stock')
def stock_form():
    return render_template('form.html')

@app.route('/stockresult', methods = ['GET'])
def stock_result():
    stock_symbol = request.args.get('amount')
    result = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%22+stock_symbol+%22&apikey=Q3TONPUKGTPM3WQQ%22")
    jsondata = result.json()

    stock_data = jsondata["Time Series (Daily)"]

    return render_template('stock_show.html',stock_symbol = stock_symbol, stock_data= stock_data)
