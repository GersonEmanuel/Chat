from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .routes.users import route

app = FastAPI()
app.include_router(route)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]

)

@app.get("/")
async def home():
    return {"message":"home page"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{data}")



