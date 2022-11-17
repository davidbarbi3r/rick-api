from fastapi import FastAPI
from routes.characters import router as char_route
from routes.episodes import router as ep_route

app = FastAPI()

app.include_router(char_route)
app.include_router(ep_route)

@app.get("/")
async def root():
    return {"message": "Hi! If you see this message that means that the API is working 🥳"}