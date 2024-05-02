from pybit.unified_trading import HTTP
from pybit.unified_trading import WebSocket
import datetime 
from datetime import datetime
import pandas as pd



########################
# Supporting functions #
########################

def convert_dt_to_timestamp(dt):
    '''
    input: string
    Timestamp('2024-02-11 15:53:59') to timestamp
    '''
    dt = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    return int(datetime.timestamp(dt)*1000)


def convert_ts_to_datetime(ts):
    '''
    1707656039991 to Timestamp('2024-02-11 15:53:59')
    '''
    return datetime.fromtimestamp(int(ts)/1000)


##############
# Bybit APIs #
##############

def get_server_time(client):
    '''
    Getting Bybit server time
    https://bybit-exchange.github.io/docs/v5/market/time 
    '''
    response = client.get_server_time()
    result = int(response.get('result').get('timeSecond'))
    result = pd.to_datetime(datetime.fromtimestamp(result))
    response_time = response.get('time')
    response_time = pd.to_datetime(datetime.fromtimestamp(int(response_time) // 1000))
    return result, response_time

def get_kline(client, category, symbol, interval, start, limit):
    '''
    Query for historical klines (also known as candles/candlesticks). 
    Charts are returned in groups based on the requested interval.
    interval: 1,3,5,15,30,60,120,240,360,720,D,M,W
    category: spot,linear,inverse
    limit for data size per page. [1, 1000]
    !!! result = start + limit units !!!
    https://bybit-exchange.github.io/docs/v5/market/kline
    '''
    response = client.get_kline(
        category = category,
        symbol = symbol,
        interval = interval,
        start = start,
        #end = end,
        limit = limit).get('result')
    data = response.get('list', None)
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
    data['datetime'] = data['timestamp'].apply(convert_ts_to_datetime)
    data.iloc[:,:-1].apply(pd.to_numeric)
    return data[['datetime', 'timestamp', 'open', 'high', 'low', 'close', 'volume',	'turnover']]

def get_mark_price_kline(client, category, symbol, interval, start, limit):
    '''
    Query for historical !mark (global spot price)! price klines. 
    Charts are returned in groups based on the requested interval.
    Product type: linear,inverse
    Kline interval: 1,3,5,15,30,60,120,240,360,720,D,M,W
    https://bybit-exchange.github.io/docs/v5/market/mark-kline
    
    '''
    response = client.get_mark_price_kline(
        category = category,
        symbol = symbol,
        interval = interval,
        start = start,
        limit = limit).get('result')
    data = response.get('list', None)
    data = pd.DataFrame(data,
                        columns =[
                            'timestamp',
                            'open',
                            'high',
                            'low',
                            'close'
                            ],
                        )
    data['datetime'] = data['timestamp'].apply(convert_ts_to_datetime)
    data.iloc[:,:-1].apply(pd.to_numeric)
    return data[['datetime', 'timestamp', 'open', 'high', 'low', 'close']]

def get_index_price_kline(client, category, symbol, interval, start, limit):
    '''
    Query for historical !index price! klines. 
    Charts are returned in groups based on the requested interval.
    https://bybit-exchange.github.io/docs/v5/market/index-kline
    '''
    response = client.get_index_price_kline(
        category = category,
        symbol = symbol,
        interval = interval,
        start = start,
        limit = limit).get('result')
    data = response.get('list', None)
    data = pd.DataFrame(data,
                        columns =[
                            'timestamp',
                            'open',
                            'high',
                            'low',
                            'close'
                            ],
                        )
    data['datetime'] = data['timestamp'].apply(convert_ts_to_datetime)
    data.iloc[:,:-1].apply(pd.to_numeric)
    return data[['datetime', 'timestamp', 'open', 'high', 'low', 'close']]

def get_premium_index_price_kline(client, category, symbol, interval, start, limit):
    '''
    Query for historical !index price! klines. 
    Charts are returned in groups based on the requested interval.
    https://bybit-exchange.github.io/docs/v5/market/index-kline
    '''
    response = client.get_premium_index_price_kline(
        category = category,
        symbol = symbol,
        interval = interval,
        start = start,
        limit = limit).get('result')
    data = response.get('list', None)
    data = pd.DataFrame(data,
                        columns =[
                            'timestamp',
                            'open',
                            'high',
                            'low',
                            'close'
                            ],
                        )
    data['datetime'] = data['timestamp'].apply(convert_ts_to_datetime)
    data.iloc[:,:-1].apply(pd.to_numeric)
    return data[['datetime', 'timestamp', 'open', 'high', 'low', 'close']]

def get_orderbook(client, category, symbol, limit):
    '''
    Query for orderbook depth data.
    Product type: spot, linear, inverse, option
    Limit size: 
    spot: [1, 200]. Default: 1.
    linear&inverse: [1, 200]. Default: 25.
    option: [1, 25]. Default: 1.
    https://bybit-exchange.github.io/docs/v5/market/orderbook 
    '''
    response = client.get_orderbook(
        category = category, 
        symbol = symbol,
        limit = limit)
    data = pd.DataFrame(data,
                        columns =[
                            'symbol',
                            'bid_buyer',
                            'bid_price',
                            'bid_size',
                            'ask_seler'
                            'ask_price',
                            'ask_size',
                            'timestamp'
                            ],
                        )    
    
def get_orderbook(client, category, symbol, limit):
    '''
    Query for orderbook depth data.
    ! I do not know why this is necessary, but may be latter... !
    https://bybit-exchange.github.io/docs/v5/market/orderbook 
    '''
    response = client.get_orderbook(
        category = category, 
        symbol = symbol,
        limit = limit).get('result')
    data = response#.get('list', None)
    data = pd.DataFrame(data,
                        columns =[
                            's',
                            'a',
                            'b',
                            'ts',
                            'u'
                            ],
                        )    
    f = lambda x: datetime.utcfromtimestamp(int(x)/1000)
    data['datetime'] = data.ts.apply(f)
    return data

def get_public_trade_history(client, category, symbol, optionType , limit):
    '''
    Query recent public trading data in Bybit.
    Actual price.
    category: spot,linear,inverse,option
    Option type. 'Call' or 'Put'. Apply to option only
    limit: 
    spot: [1,60], default: 60
    others: [1,1000], default: 500
    https://bybit-exchange.github.io/docs/v5/market/recent-trade
    '''
    response = client.get_public_trade_history(
        category = category, 
        symbol = symbol,
        limit = limit).get('result').get('list')
    data = response#.get('list', None)
    data = pd.DataFrame(data,
                        columns =[
                            'execId',
                            'symbol',
                            'price',
                            'size',
                            'side',
                            'time',
                            'isBlockTrade'
                            ],
                        )    
    f = lambda x: datetime.utcfromtimestamp(int(x)/1000)
    data['time'] = data.time.apply(f)
    return data

def get_historical_volatility(client, category, period, startTime, endTime):
    '''
    Query option historical volatility
    Only option
    Option type. 'Call' or 'Put'. Apply to option only
    https://bybit-exchange.github.io/docs/v5/market/iv
    '''
    response = client.get_historical_volatility(
        category = category, 
        period = period,
        startTime = startTime,
        endTime = endTime
        ).get('result')
    data = response#.get('list', None)
    data = pd.DataFrame(data,
                        columns =[
                            'period',
                            'value',
                            'time'
                            ],
                        )    
    f = lambda x: datetime.utcfromtimestamp(int(x)/1000)
    data['time'] = data.time.apply(f)
    return data

def get_insurance(client, coin):
    '''
    Query for Bybit insurance pool data (BTC/USDT/USDC etc). The data is updated every 24 hours.
    https://bybit-exchange.github.io/docs/v5/market/insurance 
    '''
    response = client.get_insurance(
        coin = coin, 
        ).get('result')
    data = response.get('list')
    data = pd.DataFrame(data,
                        columns =[
                            'coin',
                            'balance',
                            'value'
                            ],
                        )    
    data.loc[0, 'updatedTime'] = response.get('updatedTime')
    f = lambda x: datetime.utcfromtimestamp(int(x)/1000)
    data['updatedTime'] = data.updatedTime.apply(f)
    return data

def get_option_delivery_price(client, category, symbol, limit ):
    '''
    Get the delivery price.
    !!! Option: only returns those symbols are being "DELIVERING" (UTC8~UTC12) when "symbol" is not specified;
    https://bybit-exchange.github.io/docs/v5/market/delivery-price
    '''
    response = client.get_option_delivery_price(
        category = category,
        symbol = symbol,
        limit = limit
        ).get('result')
    data = response.get('list')
    data = pd.DataFrame(data,
                        columns =[
                            'symbol',
                            'deliveryPrice',
                            'deliveryTime'
                            ],
                        )    
    data.loc[0, 'category'] = response.get('category')
    f = lambda x: datetime.utcfromtimestamp(int(x)/1000)
    data['deliveryTime'] = data.deliveryTime.apply(f)
    return data