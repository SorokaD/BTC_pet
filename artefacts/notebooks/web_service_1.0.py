
from flask import Flask
from pybit.unified_trading import HTTP
from pybit.unified_trading import WebSocket
import pybit # working source
import pandas as pd
import time

import sys
from importlib import reload
sys.path.append('../../') 
sys.path.append('../src/')
from credentials import KEY, SECRET, KEY_test, SECRET_test
import src_API

client = HTTP(testnet=True, api_key=KEY_test, api_secret=SECRET_test)
symbol = 'BTCUSD'

app = Flask(__name__)

def foo(client, symbol):
    while True:
        print(src_API.get_data_historical(client, 'linear', symbol, '1', limit=1))
        time.sleep(5)
    #return 'foo_ok'

@app.route('/')
def hello():
    foo(client, symbol)
    return 'ok'

if __name__ == '__main__':
    app.run()