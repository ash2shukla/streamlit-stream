import asyncio

import streamlit as st
from utils import consumer


st.set_page_config(page_title="stream", layout="wide")

status = st.empty()
connect = st.checkbox("Connect to WS Server")

selected_channels = st.multiselect("Select Channels", ["A", "B", "C"], default=["A"])

columns = [col.empty() for col in st.columns(len(selected_channels))]


window_size = st.number_input("Window Size", min_value=10, max_value=100)

if connect:
    asyncio.run(consumer(dict(zip(selected_channels, columns)), selected_channels, window_size, status))
else:
    status.subheader(f"Disconnected.")