from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from wolfram_sigma_backend.app.infrastructure.chat.connection_manager import manager

chat_router = APIRouter(tags=["chat"])


@chat_router.websocket("/ws/chat/{user_name}")
async def websocket_endpoint(websocket: WebSocket, user_name: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{user_name} {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{user_name} left the chat")
