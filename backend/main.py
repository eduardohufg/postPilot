from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Imports
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

# Routes
from routes.ai import ai_router

# App
app =   FastAPI()
api = APIRouter()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Route
@app.get("/")
async def root():
    return {"message": "Server Online"}

# Routes
api.include_router(ai_router, prefix="/ai", tags=["ai"])

#includes
app.include_router(api, prefix="/api")