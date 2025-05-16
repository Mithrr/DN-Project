from fastapi import FastAPI
from Backend.API.user_routes import router as user_router
from Backend.API.svd_recommender import router as recommender_router

app = FastAPI()
app.include_router(user_router)
app.include_router(recommender_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Networking Backend"}