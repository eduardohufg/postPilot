from fastapi import APIRouter, HTTPException

ai_router = APIRouter()

@ai_router.post("/query")
async def query():
    return {"message": "Hello World"}