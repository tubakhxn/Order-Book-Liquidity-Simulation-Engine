import numpy as np
import streamlit as st

def compute_metrics(orderbook):
    bids, asks, _ = orderbook.get_state()
    spread = min(asks.index) - max(bids.index) if len(bids) > 0 and len(asks) > 0 else np.nan
    mid = (min(asks.index) + max(bids.index)) / 2 if len(bids) > 0 and len(asks) > 0 else np.nan
    total_bid_vol = bids.sum()
    total_ask_vol = asks.sum()
    # Slippage: estimate as price impact of a market order of size 100
    slippage = 0
    size = 100
    remaining = size
    for price in sorted(asks.index):
        vol = asks[price]
        if vol >= remaining:
            slippage += (price - mid) * remaining
            break
        else:
            slippage += (price - mid) * vol
            remaining -= vol
    return {
        'Spread': spread,
        'Mid Price': mid,
        'Total Bid Volume': total_bid_vol,
        'Total Ask Volume': total_ask_vol,
        'Slippage (100)': slippage
    }

def display_metrics_panel(metrics):
    st.subheader("Metrics Panel")
    for k, v in metrics.items():
        st.metric(label=k, value=f"{v:.2f}" if isinstance(v, float) else v)
