
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Rom Phirunronnakon'

@app.route('/aaaa')
def hello_world_aaaa():
    return 'the path is /aaaa'

@app.route('/aaaa/bbbb')
def hello_world_aaaa_bbbb():
    return 'the path is /aaaa/bbbb'

@app.route('/today')
def today_date():
    return str(date.today())
