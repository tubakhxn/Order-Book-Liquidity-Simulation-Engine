import plotly.graph_objs as go
import numpy as np

def plot_orderbook_3d(orderbook_history):
    # Prepare 3D surface data for bids and asks
    times = [h['time'] for h in orderbook_history]
    price_levels = orderbook_history[0]['bids'].index.tolist() + orderbook_history[0]['asks'].index.tolist()
    price_levels = sorted(set(price_levels))
    bid_vols = np.zeros((len(times), len(price_levels)))
    ask_vols = np.zeros((len(times), len(price_levels)))
    for i, h in enumerate(orderbook_history):
        for j, p in enumerate(price_levels):
            bid_vols[i, j] = h['bids'].get(p, 0)
            ask_vols[i, j] = h['asks'].get(p, 0)
    # Plotly surfaces
    fig = go.Figure()
    fig.add_trace(go.Surface(z=bid_vols, x=price_levels, y=times, colorscale='Blues', name='Bids', showscale=False, opacity=0.8))
    fig.add_trace(go.Surface(z=ask_vols, x=price_levels, y=times, colorscale='Reds', name='Asks', showscale=False, opacity=0.8))
    fig.update_layout(
        title='3D Order Book Liquidity',
        scene=dict(
            xaxis_title='Price',
            yaxis_title='Time',
            zaxis_title='Volume',
            bgcolor='#181c20',
            xaxis=dict(color='#e0e6ef'),
            yaxis=dict(color='#e0e6ef'),
            zaxis=dict(color='#e0e6ef'),
        ),
        paper_bgcolor='#181c20',
        plot_bgcolor='#181c20',
        font=dict(color='#e0e6ef'),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig
