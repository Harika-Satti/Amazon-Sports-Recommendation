import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["item_profile"])
    df.reset_index(drop=True, inplace=True)
    return df

def build_tfidf_matrix(text_series):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(text_series)
    return tfidf_matrix

def get_recommendations(df, tfidf_matrix, index, top_n=5):
    similarity_scores = cosine_similarity(
        tfidf_matrix[index], tfidf_matrix
    ).flatten()
    similar_indices = similarity_scores.argsort()[::-1][1: top_n + 1]
    result = df.iloc[similar_indices][
        ["product_id", "brand", "sport_type", "product_type", "rating"]
    ].copy()
    result["similarity"] = similarity_scores[similar_indices].round(3)
    return result
