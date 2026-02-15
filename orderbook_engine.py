import numpy as np
import pandas as pd

class OrderBookEngine:
    def __init__(self, n_levels=20, mid_price=100.0, tick_size=0.1):
        self.n_levels = n_levels
        self.mid_price = mid_price
        self.tick_size = tick_size
        self.reset()

    def reset(self):
        # Generate price levels for bids and asks, each with n_levels
        bid_prices = np.array([
            self.mid_price - (i + 1) * self.tick_size for i in range(self.n_levels)
        ])
        ask_prices = np.array([
            self.mid_price + (i + 1) * self.tick_size for i in range(self.n_levels)
        ])
        self.bids = pd.Series(
            np.random.poisson(50, self.n_levels),
            index=bid_prices
        )
        self.asks = pd.Series(
            np.random.poisson(50, self.n_levels),
            index=ask_prices
        )
        self.time = 0

    def get_state(self):
        return self.bids.copy(), self.asks.copy(), self.time

    def step(self, order_flow):
        # order_flow: dict with keys 'type', 'side', 'price', 'size'
        if order_flow['type'] == 'market':
            if order_flow['side'] == 'buy':
                # Remove from asks
                for price in self.asks.index:
                    if self.asks[price] >= order_flow['size']:
                        self.asks[price] -= order_flow['size']
                        break
                    else:
                        order_flow['size'] -= self.asks[price]
                        self.asks[price] = 0
            else:
                # Remove from bids
                for price in self.bids.index:
                    if self.bids[price] >= order_flow['size']:
                        self.bids[price] -= order_flow['size']
                        break
                    else:
                        order_flow['size'] -= self.bids[price]
                        self.bids[price] = 0
        elif order_flow['type'] == 'limit':
            if order_flow['side'] == 'buy':
                if order_flow['price'] in self.bids.index:
                    self.bids[order_flow['price']] += order_flow['size']
            else:
                if order_flow['price'] in self.asks.index:
                    self.asks[order_flow['price']] += order_flow['size']
        elif order_flow['type'] == 'cancel':
            if order_flow['side'] == 'buy':
                if order_flow['price'] in self.bids.index:
                    self.bids[order_flow['price']] = max(0, self.bids[order_flow['price']] - order_flow['size'])
            else:
                if order_flow['price'] in self.asks.index:
                    self.asks[order_flow['price']] = max(0, self.asks[order_flow['price']] - order_flow['size'])
        self.time += 1
