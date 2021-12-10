from fastapi import APIRouter
from app.api.endpoints import places 

api_router = APIRouter()

api_router.include_router(places.router, tags=["places"])