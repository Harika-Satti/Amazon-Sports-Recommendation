# SportIQ — Amazon Sports Recommendation Engine

A high-performance recommendation engine built with **FastAPI** and **scikit-learn**, using **TF-IDF Vectorization** and **Cosine Similarity** to suggest relevant sports products based on historical data.

## Project Structure
- `app.py` — FastAPI backend.
- `recommendation.py` — Core ML logic for similarity analysis.
- `index.html` — Premium animated UI for exploring recommendations.
- `Sports-Amazon dataset.csv` — The core dataset.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Backend
```bash
python app.py
```
- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Open the UI
Open `index.html` in any modern web browser.
- The UI will automatically connect to the backend if it's running (indicated by a blue "API LIVE" badge).
- If the backend is offline, the app runs in Demo Mode with built-in data.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/products` | Lists all unique product IDs. |
| GET | `/stats` | Analytics about categories, brands, and ratings. |
| GET | `/recommend/{product_id}` | Content-based recommendations for a specific product. |
| GET | `/search?q=query` | Fast keyword search across IDs, brands, and sports. |

## How it Works
1. **Data Preprocessing**: Loads Amazon sports product data and combines key features into an *item profile*.
2. **Vectorization**: Uses `TfidfVectorizer` to convert text descriptions into mathematical vectors.
3. **Similarity**: Calcluates `Cosine Similarity` between vectors to find products with the most similar profiles.
4. **Ranking**: Returns the top $N$ most similar products with a confidence score.
