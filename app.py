import streamlit as st
from orderbook_engine import OrderBookEngine
from simulation import OrderBookSimulation
from visualization import plot_orderbook_3d
from metrics import compute_metrics, display_metrics_panel

st.set_page_config(
    page_title="3D Order Book Liquidity Engine",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📈"
)

# --- Dark Institutional Theme ---
st.markdown(
    """
    <style>
    body, .stApp { background-color: #181c20; color: #e0e6ef; }
    .stSidebar { background-color: #23272b; }
    .st-bb, .st-cq, .st-cv, .st-cw { background: #23272b !important; }
    .stButton>button { background: #2b3137; color: #e0e6ef; }
    .stSlider>div>div { background: #23272b; }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Controls ---
st.sidebar.title("Simulation Controls")
volatility = st.sidebar.slider("Volatility", 0.01, 0.10, 0.03, 0.01)
order_rate = st.sidebar.slider("Order Arrival Rate", 1, 20, 5, 1)
market_order_size = st.sidebar.number_input("Market Order Size", 1, 1000, 100)
sim_speed = st.sidebar.slider("Simulation Speed (ms/step)", 100, 2000, 500, 100)

# --- Initialize Simulation ---
if 'sim' not in st.session_state:
    st.session_state.sim = OrderBookSimulation(
        volatility=volatility,
        order_rate=order_rate,
        market_order_size=market_order_size
    )

sim = st.session_state.sim
sim.update_params(volatility, order_rate, market_order_size)

# --- Main Layout ---
st.title("3D Order Book Liquidity Engine")

col1, col2 = st.columns([3, 1])

with col1:
    fig = plot_orderbook_3d(sim.orderbook_history)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    metrics = compute_metrics(sim.orderbook)
    display_metrics_panel(metrics)

# --- Animation Loop ---
if st.button("Step Simulation"):
    sim.step()
    st.experimental_rerun()

if st.button("Run Animation"):
    import time
    for _ in range(20):
        sim.step()
        time.sleep(sim_speed / 1000)
        st.experimental_rerun()
