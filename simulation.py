import numpy as np
from orderbook_engine import OrderBookEngine

class OrderBookSimulation:
    def __init__(self, volatility=0.03, order_rate=5, market_order_size=100):
        self.volatility = volatility
        self.order_rate = order_rate
        self.market_order_size = market_order_size
        self.orderbook = OrderBookEngine()
        self.orderbook_history = []
        self.reset()

    def reset(self):
        self.orderbook.reset()
        self.orderbook_history = []
        self._record_state()

    def update_params(self, volatility, order_rate, market_order_size):
        self.volatility = volatility
        self.order_rate = order_rate
        self.market_order_size = market_order_size

    def step(self):
        # Simulate random order flow
        for _ in range(self.order_rate):
            order_type = np.random.choice(['market', 'limit', 'cancel'], p=[0.3, 0.5, 0.2])
            side = np.random.choice(['buy', 'sell'])
            price_shift = np.random.normal(0, self.volatility)
            mid = self.orderbook.mid_price + price_shift
            if order_type == 'market':
                order = {'type': 'market', 'side': side, 'size': self.market_order_size}
            else:
                price = mid + np.random.randint(-5, 6) * self.orderbook.tick_size
                size = np.random.poisson(20)
                order = {'type': order_type, 'side': side, 'price': price, 'size': size}
            self.orderbook.step(order)
        self._record_state()

    def _record_state(self):
        bids, asks, t = self.orderbook.get_state()
        self.orderbook_history.append({'bids': bids.copy(), 'asks': asks.copy(), 'time': t})
