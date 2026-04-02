from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
from recommendation import load_data, build_tfidf_matrix, get_recommendations

app = FastAPI(title="Amazon Sports Recommendation", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data at startup
df = load_data("Sports-Amazon dataset.csv")
tfidf_matrix = build_tfidf_matrix(df["item_profile"])

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/products")
def get_products():
    products = df["product_id"].unique().tolist()
    return {"products": products, "total": len(products)}

@app.get("/stats")
def get_stats():
    return {
        "total_records": int(df.shape[0]),
        "total_products": int(df["product_id"].nunique()),
        "sport_types": df["sport_type"].value_counts().to_dict(),
        "brands": df["brand"].value_counts().head(10).to_dict(),
        "avg_rating": round(float(df["rating"].mean()), 2),
    }

@app.get("/recommend/{product_id}")
def recommend(product_id: str, top_n: int = 5):
    if product_id not in df["product_id"].values:
        raise HTTPException(status_code=404, detail="Product not found")
    if top_n < 1 or top_n > 20:
        raise HTTPException(status_code=400, detail="top_n must be between 1 and 20")
    
    index = df.index[df["product_id"] == product_id][0]
    result = get_recommendations(df, tfidf_matrix, index, top_n)
    
    product_info = df[df["product_id"] == product_id].iloc[0]
    
    return {
        "query_product": {
            "product_id": product_id,
            "brand": product_info["brand"],
            "sport_type": product_info["sport_type"],
            "product_type": product_info["product_type"],
            "rating": float(product_info["rating"]),
        },
        "recommendations": result.to_dict(orient="records"),
        "count": len(result),
    }

@app.get("/search")
def search(q: str, limit: int = 20):
    mask = (
        df["product_id"].str.contains(q, case=False, na=False) |
        df["brand"].str.contains(q, case=False, na=False) |
        df["sport_type"].str.contains(q, case=False, na=False) |
        df["product_type"].str.contains(q, case=False, na=False)
    )
    results = df[mask].drop_duplicates("product_id").head(limit)
    return {"results": results[["product_id", "brand", "sport_type", "product_type", "rating"]].to_dict(orient="records")}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
