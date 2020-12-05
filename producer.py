from fastapi import FastAPI, WebSocket
from random import choice, randint
import asyncio


app = FastAPI()

CHANNELS = ["A", "B", "C"]

@app.websocket("/sample")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_json({
            "channel": choice(CHANNELS),
            "data": randint(1, 10)
            }
        )
        await asyncio.sleep(0.5)
