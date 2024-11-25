# Main run file for the for the trade project
import time
import os
from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import requests

from config import SYMBOL, CATEGORY, DELAY, MARK_AND_LAST_PRICE_DIFF, NUMBER_OF_ORDERS

from tumar.src.trading import Market

load_dotenv()

session_main = HTTP(testnet=True, api_key=os.getenv('BYBIT_KEY_test'), api_secret=os.getenv('BYBIT_SECRET_test'))
symbol = SYMBOL
delay = DELAY
category = CATEGORY

market_btc = Market(session_main, category=category, symbol=symbol)


def main():
    while True:
        try:
            orders = market_btc.get_open_orders()
            orders_data = orders.get('result').get('list')
            if len(orders_data) < NUMBER_OF_ORDERS:
                price = market_btc.get_tickers()
                price_mark = price.get('result').get('list')[0].get('markPrice')
                price_last = price.get('result').get('list')[0].get('lastPrice')
                index_diff = abs(float(price_last) - float(price_mark)) / float(price_last) * 100
                if index_diff > MARK_AND_LAST_PRICE_DIFF:
                    print(f"Mark price is {round(index_diff,2)}% higher than last price. Skip order.")
                    time.sleep(delay)
                    continue
                price_data = {'category': price.get('result').get('category'),
                              'symbol': price.get('result').get('list')[0].get('symbol'),
                              'price' : price.get('result').get('list')[0].get('markPrice'),
                              'time' : price.get('time'),
                              }
                order = requests.post('http://localhost:9090/predict_btcusdt', json=price_data)
                print(f'Открыт ордер {order}')
            print("Ожидаем закрытия позиции")
        except KeyboardInterrupt:
            print("Program stopped by user.")
            break
    return 'end'


if __name__ == "__main__":
    main()
