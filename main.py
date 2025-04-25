from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

@app.get("/")
async def get_time():
    return {"current_time": datetime.now().isoformat()}

@app.post("/")
async def post_time(request: Request):
    # Accept any JSON body but ignore it
    _ = await request.json()
    return {"current_time": datetime.now().isoformat()}
