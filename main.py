import asyncio

import aiohttp
import streamlit as st
from collections import deque, defaultdict
from functools import partial


WS_CONN = "ws://localhost:5050/sample"

async def consumer(graph, selected_channels, window_size, status):
    windows = defaultdict(partial(deque, [0]*window_size, maxlen=window_size))

    async with aiohttp.ClientSession(trust_env = True) as session:
        status.subheader(f"Connecting to {WS_CONN}")
        async with session.ws_connect(WS_CONN) as websocket:
            status.subheader(f"Connected to: {WS_CONN}")
            async for message in websocket:
                data = message.json()

                if data["channel"] in selected_channels:
                    windows[data["channel"]].append(data["data"])

                graph.line_chart(windows)

status = st.empty()
graph = st.empty()

connect = st.checkbox("Connect to WS Server")
selected_channels = st.multiselect("Select Channels", ["A", "B", "C"])

window_size = st.number_input("Window Size", min_value=10, max_value=100)

if connect:
    asyncio.run(consumer(graph, selected_channels, window_size, status))
else:
    status.subheader(f"Disconnected from: {WS_CONN}")