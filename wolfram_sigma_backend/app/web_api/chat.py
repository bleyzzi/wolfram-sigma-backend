from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends

from wolfram_sigma_backend.app.auth.auth import current_user
from wolfram_sigma_backend.app.infrastructure.chat.connection_manager import ConnectionManager
from wolfram_sigma_backend.app.models.auth_models import User

chat_router = APIRouter(tags=["chat"], dependencies=[Depends(current_user)])


@chat_router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket, user: User = Depends(current_user)):
    manager = ConnectionManager()
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{user.username} {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{user.username} left the chat")
