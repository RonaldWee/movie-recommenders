import pickle
from surprise import Dataset, Reader, SVD, KNNBasic, SlopeOne, BaselineOnly, CoClustering
import pandas as pd
from surprise.model_selection import train_test_split

# Load ratings
ratings = pd.read_csv("/home/ronald/movie-lens-dataset/backend/data/ratings.csv")
reader = Reader(rating_scale=(0.5, 5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

trainset, _ = train_test_split(data, test_size=0.2)

models = {
    'SVD': SVD(),
    'KNN Basic': KNNBasic(sim_options={"name": "cosine", "user_based": True}),
    'KNN Item': KNNBasic(sim_options={"name": "cosine", "user_based": False}),
    'Slope One': SlopeOne(),
    'BaselineOnly': BaselineOnly(),
    'CoClustering': CoClustering()
}

# Train and save
for name, model in models.items():
    print(f"Training {name}...")
    model.fit(trainset)
    with open(f"/home/ronald/movie-lens-dataset/models/{name}.pkl", "wb") as f:
        pickle.dump(model, f)
    print(f"Saved {name} to models/{name}.pkl")
