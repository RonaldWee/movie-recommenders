import pickle
import os
import pandas as pd

# Load movies & ratings for recommendation function
ratings = pd.read_csv("/home/ronald/movie-lens-dataset/backend/data/ratings.csv")
movies = pd.read_csv("/home/ronald/movie-lens-dataset/backend/data/movies.csv")

# Load models from disk
MODEL_NAMES = ['SVD', 'KNN Basic', 'KNN Item', 'Slope One', 'BaselineOnly', 'CoClustering']
models = {}

for name in MODEL_NAMES:
    path = f"/home/ronald/movie-lens-dataset/models/{name}.pkl"
    if os.path.exists(path):
        with open(path, "rb") as f:
            models[name] = pickle.load(f)
        print(f"Loaded model: {name}")
    else:
        print(f"Model {name} not found. Please train it first.")

# Recommendation logic
def get_recommendations(user_id, model, top_n=5):
    user_movies = ratings[ratings['userId'] == user_id]['movieId'].tolist()
    all_movies = movies[~movies['movieId'].isin(user_movies)].copy()

    all_movies['est'] = all_movies['movieId'].apply(lambda x: model.predict(user_id, x).est)
    top_movies = all_movies.sort_values(by='est', ascending=False).head(top_n)
    
    return top_movies[['movieId', 'title']].to_dict(orient='records')
