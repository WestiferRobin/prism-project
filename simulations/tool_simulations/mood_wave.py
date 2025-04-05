import uvicorn
from fastapi import FastAPI

mood_api = FastAPI()

@mood_api.get("/mood/test")
async def test_mood_wave():
    return "MOOD WAVE!!!!!"

def run_mood_wave():
    uvicorn.run(mood_api, host="127.0.0.1", port=8000)
