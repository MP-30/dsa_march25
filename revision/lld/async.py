# Write an asynchronous WebSocket server handler using Python (asyncio/FastAPI) to stream live biofeedback metrics to a coach dashboard.

from fastapi import FastAPI, WebSocket

app= FastApi()

@app.websocket("/ws/{id}")
async def websocket_endpoint(
        websocket: WebSocket,
        id: int,
):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            metrics = {
                "athlete_id": id,
                "heart_rate": data["heart_rate"],
            }
            await  websocket.send_json(metrics)
    except Exception:
        await websocket.close()