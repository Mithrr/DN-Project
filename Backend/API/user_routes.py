# Backend/API/user_routes.py
from fastapi import APIRouter
from pymongo import MongoClient
from Backend.API.svd_recommender import get_recommendations

router = APIRouter()

# Setup MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client["The_DN_project"]
collection = db["users"]

@router.post("/register")
async def register_user(user: dict):
    result = collection.insert_one(user)
    return {
        "status": "user registered",
        "inserted_id": str(result.inserted_id)
    }


@router.get("/recommend/{user_name}")
async def recommend_users(user_name: str):
    return get_recommendations(user_name)