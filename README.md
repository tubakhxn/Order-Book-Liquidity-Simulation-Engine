
# 3D Order Book Liquidity Engine

## Developer/Creator
**tubakhxn**
<img width="2773" height="1537" alt="order" src="https://github.com/user-attachments/assets/5773e635-3d39-4eb4-a8d0-451c0093bc7a" />


An interactive Streamlit app to simulate and visualize a 3D limit order book, modeling market microstructure and liquidity dynamics.

## Features
- Synthetic limit order book simulation (bids, asks, order flow)
- Models for order flow imbalance (OFI), bid-ask spread, liquidity depth, and slippage
- 3D Plotly visualization (price, time, volume)
- Interactive controls for volatility, order arrival, market order size, and simulation speed
- Animated liquidity changes and collapse events
- Metrics panel: spread, mid price, total bid/ask volume, slippage
- Dark institutional theme

## Microstructure Concepts
- **Limit Order Book (LOB):** Centralized record of buy (bid) and sell (ask) orders at different price levels.
- **Order Flow Imbalance (OFI):** Difference between aggressive buy and sell orders, indicating pressure on price movement.
- **Bid-Ask Spread:** Difference between the lowest ask and highest bid, representing transaction cost and liquidity.
- **Liquidity Depth:** Volume available at each price level; deeper books are more resilient to large orders.
- **Slippage:** The difference between expected and actual execution price, often due to insufficient liquidity.

## Tech Stack
- Streamlit, NumPy, Pandas, Plotly, SciPy

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `streamlit run app.py`

---
Professional, modular code. See source files for details.

## How to Fork
1. Click the "Fork" button at the top right of the GitHub repository page.
2. Clone your forked repository:
	```
	git clone https://github.com/<your-username>/<repo-name>.git
	```
3. Create your own branch for changes:
	```
	git checkout -b my-feature
	```
4. Push changes and submit a pull request to contribute.

