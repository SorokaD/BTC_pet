from pybit.unified_trading import HTTP
from pybit.unified_trading import WebSocket
import datetime as dt

import pandas as pd

def get_data_historical(client, category, symbol, interval, start = None, end = None, limit=1000):
    '''
    function are returned frame in groups based on the requested interval
    interval: 1,3,5,15,30,60,120,240,360,720,D,M,W
    category: spot,linear,inverse
    limit for data size per page. [1, 1000]
    https://bybit-exchange.github.io/docs/v5/market/kline#http-request
    '''
    response = client.get_kline(category=category, 
                             symbol = symbol, 
                             interval = interval, 
                             start = start,
                             end = end,
                             limit = limit).get('result')
    data = response.get('list', None)
    if not data:
        return 
    data = pd.DataFrame(data,
                        columns =[
                            'timestamp',
                            'open',
                            'high',
                            'low',
                            'close',
                            'volume',
                            'turnover'
                            ],
                        )
    f = lambda x: dt.datetime.utcfromtimestamp(int(x)/1000)
    data.index = data.timestamp.apply(f)
    return data[::-1].apply(pd.to_numeric)


    

