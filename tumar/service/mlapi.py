import logging
import os
from contextlib import asynccontextmanager

from pybit.unified_trading import HTTP
from dotenv import load_dotenv

import uvicorn
import yaml
from fastapi import FastAPI, HTTPException, Request, status, Depends

import sentry_sdk

from models import ModelRequest, ModelResponse
from tumar.src.trading import Trade, Market
# TODO: $env:PYTHONPATH="D:\myGit\Tumar"

from config import CATEGORY

load_dotenv()

sentry_sdk.init(dsn="https://e267c2bc7bd8ffe2c76c633241bf59c7@o4508301452771328.ingest.de.sentry.io/4508301457358928",)
session_ml = HTTP(testnet=True, api_key=os.getenv('BYBIT_KEY_test'), api_secret=os.getenv('BYBIT_SECRET_test'))

logger = logging.getLogger("mlapi")

app = FastAPI(title="ML Application", debug=True)
trade_btc = Trade(session_ml, symbol="BTCUSDT")
market_btc = Market(session_ml, category=CATEGORY, symbol="BTCUSDT")

# counter
class CounterState:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1
        return self.counter

# Создаем глобальный объект состояния
counter_state = CounterState()

def get_counter_state():
    return counter_state
# counter


@app.get("/healthcheck")
def check_connection():
    """
    Check connection
    
    Args: none

    Returns: status code
    """
    return status.HTTP_200_OK


@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


@app.post("/predict_btcusdt")
async def predict_btcusdt(request: ModelRequest, counter: CounterState = Depends(get_counter_state)) -> ModelResponse:
    """
    Predict BTCUSDT
    """
    qty = 0.001
    price = request.price
    orders = market_btc.get_open_orders()
    side = trade_btc.get_side_decision(orders)
    take_profit, stop_loss = trade_btc.get_tpsl_interval(price=price, side=side)
    try:
        order = trade_btc.order_place(side=side, qty=qty, stop_loss=stop_loss, take_profit=take_profit)
    except Exception as e:
        logger.error(f"Failed to place order: {e}")
        raise HTTPException(status_code=500, detail="Failed to place order")
    use_predict = True
    symbol = request.symbol
    current_counter = counter.increment()  # Увеличиваем счетчик
    print(f"Попытка размещения ордера {order}. По счету {current_counter}")
    return ModelResponse(use_predict=use_predict, symbol=symbol, side=side, quantity=qty)


def main():
    uvicorn.run("mlapi:app", host="127.0.0.1", port=9090, access_log=True, use_colors=False, reload=True)


if __name__ == "__main__":
    main()
