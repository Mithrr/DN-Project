from fastapi import APIRouter
from pymongo import MongoClient
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

router = APIRouter()

client = MongoClient("mongodb://localhost:27017/")
db = client["The_DN_project"]
collection = db["users"]

@router.get("/recommend/{user_name}")
def get_recommendations(user_name: str):
    users = list(collection.find())
    if not users:
        return {"error": "No users found"}

    # Collect unique tags
    tags = set()
    for user in users:
        tags.update(user.get("Interested_Fields", {}).get("Require", []))
        tags.update(user.get("Interested_Fields", {}).get("Seek", []))
    tags = list(tags)

    # Create vectors
    user_vectors, user_names, user_docs = [], [], []
    for user in users:
        vector = [0] * len(tags)
        for i, tag in enumerate(tags):
            if tag in user.get("Interested_Fields", {}).get("Require", []) or tag in user.get("Interested_Fields", {}).get("Seek", []):
                vector[i] = 1
        user_vectors.append(vector)
        user_names.append(user.get("Name", f"Unknown_{len(user_names)}"))
        user_docs.append(user)

    df = pd.DataFrame(user_vectors, index=user_names, columns=tags)

    if user_name not in df.index:
        return {"error": f"User '{user_name}' not found"}

    user_index = df.index.tolist().index(user_name)
    user_doc = users[user_index]

    # Apply SVD and compute cosine similarity
    svd = TruncatedSVD(n_components=min(2, len(tags) - 1 if len(tags) > 1 else 1))
    reduced_matrix = svd.fit_transform(df)
    sim_matrix = cosine_similarity(reduced_matrix)

    # Interest-based matches
    interest_matches = []
    for idx, score in enumerate(sim_matrix[user_index]):
        if idx != user_index and score > 0:
            interest_matches.append({
                "name": df.index[idx],
                "score": round(score, 2),
                "type": "interest_match"
            })

    # Investor matches
    required_amount = user_doc.get("Investment_Required", 0)
    investor_matches = []

    if user_doc.get("User_Type") == "Requirement" and required_amount > 0:
        for user in users:
            if user.get("User_Type") == "Investor":
                capacity = user.get("Investment_Capacity", 0)
                if capacity >= required_amount:
                    investor_matches.append({
                        "name": user["Name"],
                        "score": 0.5,  # lower than shared interest matches
                        "type": "investor_match"
                    })

    # Merge and sort
    combined = interest_matches + investor_matches
    combined_sorted = sorted(combined, key=lambda x: x["score"], reverse=True)[:10]

    return {
        "user": user_name,
        "recommendations": combined_sorted
    }