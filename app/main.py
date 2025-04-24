from fastapi import FastAPI
import asyncio
from app.bot.bot import start_bot  

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_bot())

@app.get("/")
def read_root():
    return {"msg": "FURIA Bot está no ar!"}
