from time import time
import random


class Market:
    def __init__(self, session, category, symbol):
        self.session = session
        self.symbol = symbol
        self.category = category

    def get_tickers(self):
        """
        Get tickers
        """
        tickers = self.session.get_tickers(category=self.category, symbol=self.symbol)
        return tickers

    def get_open_orders(self):
        """
        Get open orders
        """
        orders = self.session.get_open_orders(symbol=self.symbol, category=self.category)
        return orders


class Trade:
    def __init__(self, session, symbol):
        self.session = session
        self.symbol = symbol

    def order_place(self, side, qty, stop_loss, take_profit):
        """
        Place an order with take profit and stop loss
        """
        positionIdx = 1 if side == "Buy" else 2
        orderLinkId = f"{self.symbol}-{side}-{int(time())}"
        order = self.session.place_order(
            category="linear",
            symbol=self.symbol,
            side=side,
            orderType="Market",
            qty=qty,
            takeProfit=take_profit,
            stopLoss=stop_loss,
            positionIdx=positionIdx,
            orderLinkId=orderLinkId,
        )
        return order

    def get_tpsl_interval(self, price, side):
        """
        Get take profit and stop loss interval
        """
        profit = 1000  # ???
        loss = 5000  # ???
        if side == "Buy":
            take_profit = price + profit
            stop_loss = price - loss
        elif side == "Sell":
            take_profit = price - profit
            stop_loss = price + loss
        else:
            raise ValueError("Side must be either 'Buy' or 'Sell'")
        return take_profit, stop_loss

    def get_side_decision(self, orders):
        """
        Get decision
        """
        positions = {'Buy', 'Sell'}
        current_opened_positions = set([x.get('side') for x in orders.get('result').get('list')])  # looking for list of open positions
        decision = list(current_opened_positions)[0] if len(current_opened_positions) > 0 else random.choice(list(positions))
        print(decision)
        return decision


class Position:
    pass
