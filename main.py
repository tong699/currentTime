from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

@app.get("/")
async def get_time():
    return {"current_time": datetime.now().isoformat()}

@app.post("/")
async def post_time(request: Request):
    try:
        await request.json()  # Try parsing JSON, even if we ignore it
    except Exception:
        pass  # Ignore any parsing errors
    return {"current_time": datetime.now().isoformat()}

