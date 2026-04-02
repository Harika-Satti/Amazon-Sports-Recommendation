<!-- 🔥 Animated Header -->
<h1 align="center">🚀 SportIQ</h1>
<h3 align="center">Amazon Sports Recommendation Engine</h3>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=22&duration=3000&color=00BFFF&center=true&vCenter=true&width=600&lines=AI+Powered+Recommendation+System;FastAPI+%7C+Machine+Learning+%7C+NLP;Built+by+Harika+Satti" />
</p>

## 🏷️ Badges

<p align="center">
  <img src="https://img.shields.io/badge/Live-Demo-green?style=for-the-badge&logo=render" />
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-teal?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Deployed%20on-Render-black?style=for-the-badge&logo=render" />
</p>

<p align="center">
  🔗 <b>Live App:</b> https://your-app.onrender.com
</p>

## ✨ Overview

**SportIQ** is a high-performance recommendation engine that delivers **personalized sports product suggestions** using **NLP and Machine Learning**.

It uses **TF-IDF Vectorization** and **Cosine Similarity** to recommend products based on content similarity.


## 🎯 Features

- 🔍 Smart Content-Based Recommendations  
- ⚡ FastAPI High-Speed Backend  
- 🧠 NLP-based Similarity Engine  
- 📊 Real-time Product Insights  
- 🎨 Interactive UI with animations  
- 🟢 Demo Mode support  

## 🖼️ Screenshots

### 🏠 Home Page
<img src="screenshots/dashboard1.png" width="800"/>
<img src="screenshots/dashboard2.png" width="800"/>

### 🎯 Recommendations
<img src="screenshots/result1.png" width="800"/>
<img src="screenshots/result2.png" width="800"/>

### 📊 API Docs
<img src="screenshots/API1.png" width="800"/>
<img src="screenshots/API2.png" width="800"/>
## 🌐 Live Demo Preview

### 🏠 Home Page (Live)
<img src="page.png" width="900"/>
<img src="live.png" width="900"/>

🔗 https://amazon-sports-recommendation.onrender.com

### 📊 API Documentation (FastAPI Swagger)
<img src="livedocs.png" width="900"/>

🔗 https://amazon-sports-recommendation.onrender.com/docs


## 🏗️ Project Structure

SportIQ/
│
├── app.py
├── recommendation.py
├── index.html
├── requirements.txt
├── Sports-Amazon dataset.csv


## ⚙️ Tech Stack

- **Backend:** FastAPI  
- **ML:** scikit-learn  
- **Data:** pandas, numpy  
- **NLP:** TF-IDF  
- **Similarity:** Cosine Similarity  

## 🚀 Getting Started

### Install Dependencies

bash
pip install -r requirements.txt

### Run Backend

bash
python app.py

📍 API: http://localhost:8000  
📘 Docs: http://localhost:8000/docs  

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /products | Get all products |
| GET | /stats | Dataset insights |
| GET | /recommend/{id} | Recommendations |
| GET | /search?q= | Search |

## 🧠 How It Works

- Combines product features (title, category, brand)  
- Converts text → vectors using TF-IDF  
- Computes similarity using cosine distance  
- Returns top-N recommendations  

## 📊 Sample Output
json
{
  "product_id": "SP123",
  "recommendations": [
    {"id": "SP456", "score": 0.87},
    {"id": "SP789", "score": 0.82}
  ]
}
## 🌐 Deployment

Deployed on **Render**

bash
gunicorn app:app

## 💡 Future Enhancements

- 🔮 Hybrid Recommendation System  
- 🤖 Deep Learning (BERT)  
- 📱 Mobile Optimization  
- 👤 User Personalization  

## 👩‍💻 Author

**Harika Satti**  
Aspiring Data Scientist 🚀  

⭐ If you like this project, give it a star!
