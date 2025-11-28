# Movie Recommender System - Complete Documentation

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Dataset Information](#dataset-information)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Recommendation Algorithms](#recommendation-algorithms)
- [Model Training](#model-training)
- [Performance Metrics](#performance-metrics)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## Overview

This is a full-stack movie recommendation system that leverages collaborative filtering techniques to provide personalized movie recommendations. The system compares multiple recommendation algorithms and provides an interactive web interface for users to explore recommendations.

### Key Features
- Multiple collaborative filtering algorithms (SVD, KNN, Slope One, etc.)
- RESTful API backend built with Flask
- Modern React frontend with real-time recommendations
- Comprehensive model evaluation with precision/recall metrics
- Pre-trained models for instant recommendations

## Architecture

The system follows a three-tier architecture:

```
┌─────────────────┐
│  React Frontend │  (Port 3000)
│   (User Input)  │
└────────┬────────┘
         │ HTTP Request
         ▼
┌─────────────────┐
│   Flask Backend │  (Port 5000)
│   (API Server)  │
└────────┬────────┘
         │ Model Prediction
         ▼
┌─────────────────┐
│  Pre-trained ML │
│     Models      │
│   (.pkl files)  │
└─────────────────┘
```

### Data Flow
1. User enters User ID and selects algorithm in React UI
2. Frontend sends GET request to `/recommend` endpoint
3. Backend loads appropriate model from disk
4. Model generates top-N recommendations for the user
5. Backend returns movie titles and IDs as JSON
6. Frontend displays recommendations to user

## Features

### Implemented
- Six collaborative filtering algorithms
- User-based and item-based recommendations
- Real-time recommendation generation
- Algorithm comparison interface
- Model persistence (pickle serialization)
- Cross-validation evaluation metrics

### Algorithms Supported
1. **SVD** (Singular Value Decomposition)
2. **KNN Basic** (User-based collaborative filtering)
3. **KNN Item** (Item-based collaborative filtering)
4. **Slope One** (Weighted slope one algorithm)
5. **BaselineOnly** (Baseline estimates using ALS)
6. **CoClustering** (Co-clustering algorithm)

## Technology Stack

### Backend
- **Python 3.7+**
- **Flask 2.2.5** - Web framework
- **scikit-surprise 1.1.1** - Recommendation algorithms
- **pandas 1.3.5** - Data manipulation
- **numpy 1.21.6** - Numerical computing

### Frontend
- **React 19.1.0** - UI framework
- **React Scripts 5.0.1** - Build tooling
- **Modern JavaScript (ES6+)**

### Development Tools
- **Jupyter Notebook** - Model experimentation
- **matplotlib/seaborn** - Visualization
- **Git** - Version control

## Dataset Information

### MovieLens Small Dataset
- **Source**: GroupLens Research (University of Minnesota)
- **Size**: ml-latest-small
- **Ratings**: 100,836 ratings
- **Movies**: 9,742 movies
- **Users**: 610 users
- **Rating Scale**: 0.5 to 5.0 (half-star increments)
- **Time Period**: March 1996 - September 2018

### Dataset Files
```
backend/data/
├── ratings.csv    # userId, movieId, rating, timestamp
├── movies.csv     # movieId, title, genres
├── links.csv      # movieId, imdbId, tmdbId
└── tags.csv       # userId, movieId, tag, timestamp
```

### Citation
Harper, F. M., & Konstan, J. A. (2015). The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS), 5(4), 19:1-19:19.

## Project Structure

```
movie-recommenders/
│
├── backend/
│   ├── app.py              # Flask API server
│   ├── recommender.py      # Recommendation logic & model loading
│   └── data/
│       ├── ratings.csv     # User-movie ratings
│       ├── movies.csv      # Movie metadata
│       └── README.txt      # Dataset documentation
│
├── frontend/
│   ├── package.json        # Node dependencies
│   ├── public/             # Static assets
│   └── src/
│       ├── App.js          # Main React component
│       ├── App.css         # Styling
│       └── index.js        # React entry point
│
├── models/
│   ├── SVD.pkl                    # Trained SVD model (~10 MB)
│   ├── KNN Basic.pkl              # User-based KNN (~6 MB)
│   ├── KNN Item.pkl               # Item-based KNN (~646 MB)
│   ├── Slope One.pkl              # Slope One model (~1.3 GB)
│   ├── BaselineOnly.pkl           # Baseline model (~3 MB)
│   ├── CoClustering.pkl           # CoClustering model (~3 MB)
│   └── train_and_save_models.py  # Model training script
│
├── myenv/                  # Python virtual environment
├── Model_Losses.ipynb     # Model evaluation notebook
├── requirements.txt       # Python dependencies
├── README.md             # Quick start guide
└── DOCUMENTATION.md      # This file
```

## Installation

### Prerequisites
- Python 3.7 or higher
- Node.js 14 or higher
- npm 6 or higher
- Git

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommenders.git
cd movie-recommenders
```

#### 2. Set Up Python Backend
```bash
# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate  # On Linux/Mac
# or
myenv\Scripts\activate     # On Windows

# Install Python dependencies
pip install -r requirements.txt
```

#### 3. Set Up React Frontend
```bash
cd frontend
npm install
cd ..
```

#### 4. Verify Dataset Location
Ensure the dataset files are present in `backend/data/`:
- ratings.csv
- movies.csv
- links.csv (optional)
- tags.csv (optional)

#### 5. Train Models (if needed)
```bash
cd models
python train_and_save_models.py
cd ..
```

**Note**: Pre-trained models are included. Training takes ~10-30 minutes depending on hardware.

## Usage

### Running the Application

#### Terminal 1: Start Backend Server
```bash
cd backend
source ../myenv/bin/activate  # Activate venv if not already active
python app.py
```
Backend will run on `http://localhost:5000`

#### Terminal 2: Start Frontend Server
```bash
cd frontend
npm start
```
Frontend will run on `http://localhost:3000` and automatically open in browser.

### Using the Web Interface

1. **Enter User ID**: Type a user ID (1-610) in the input field
2. **Select Algorithm**: Choose from the dropdown:
   - SVD (recommended for accuracy)
   - KNN Basic (user-based)
   - KNN Item (item-based)
   - Slope One
   - BaselineOnly
   - CoClustering
3. **Get Recommendations**: Click "Get Recommendations" button
4. **View Results**: Top 5 movie recommendations will be displayed

### Example User IDs
- User 1: Active user with many ratings
- User 100: Moderate user
- User 500: Different taste profile

## API Reference

### Endpoint: GET /recommend

Generates personalized movie recommendations for a user.

#### Request Parameters
| Parameter | Type    | Required | Description                      |
|-----------|---------|----------|----------------------------------|
| user_id   | integer | Yes      | User ID (1-610)                  |
| algo      | string  | No       | Algorithm name (default: "SVD")  |

#### Supported Algorithm Values
- `"SVD"`
- `"KNN Basic"`
- `"KNN Item"`
- `"Slope One"`
- `"BaselineOnly"`
- `"CoClustering"`

#### Example Request
```bash
curl "http://localhost:5000/recommend?user_id=1&algo=SVD"
```

#### Success Response (200 OK)
```json
[
  {
    "movieId": 318,
    "title": "Shawshank Redemption, The (1994)"
  },
  {
    "movieId": 858,
    "title": "Godfather, The (1972)"
  },
  {
    "movieId": 50,
    "title": "Usual Suspects, The (1995)"
  },
  {
    "movieId": 527,
    "title": "Schindler's List (1993)"
  },
  {
    "movieId": 1221,
    "title": "Godfather: Part II, The (1974)"
  }
]
```

#### Error Response (400 Bad Request)
```json
{
  "error": "Algorithm 'InvalidAlgo' not found."
}
```

## Recommendation Algorithms

### 1. SVD (Singular Value Decomposition)
**Type**: Matrix factorization
**Best For**: General-purpose recommendations
**Characteristics**:
- Decomposes user-item rating matrix into latent factors
- Handles sparse data well
- Fast prediction time
- Good balance of accuracy and performance

**Implementation**: `surprise.SVD()`

### 2. KNN Basic (User-based)
**Type**: Neighborhood-based collaborative filtering
**Best For**: Finding similar users
**Characteristics**:
- Computes user-user cosine similarity
- Recommends items liked by similar users
- Memory-intensive (stores similarity matrix)
- Good for cold-start users with some ratings

**Implementation**: `KNNBasic(sim_options={"name": "cosine", "user_based": True})`

### 3. KNN Item (Item-based)
**Type**: Neighborhood-based collaborative filtering
**Best For**: Finding similar movies
**Characteristics**:
- Computes item-item cosine similarity
- Recommends similar items to what user has liked
- Very large model size (~646 MB)
- Stable recommendations over time

**Implementation**: `KNNBasic(sim_options={"name": "cosine", "user_based": False})`

### 4. Slope One
**Type**: Item-based collaborative filtering
**Best For**: Simplicity and interpretability
**Characteristics**:
- Computes average rating differences between items
- Simple to understand and implement
- Large model size (~1.3 GB)
- Good for sparse datasets

**Implementation**: `surprise.SlopeOne()`

### 5. BaselineOnly
**Type**: Baseline estimates
**Best For**: Baseline comparison
**Characteristics**:
- Uses user and item biases
- ALS (Alternating Least Squares) optimization
- Fast and lightweight (~3 MB)
- Good starting point for hybrid systems

**Implementation**: `surprise.BaselineOnly()`

### 6. CoClustering
**Type**: Co-clustering
**Best For**: Finding user-item clusters
**Characteristics**:
- Simultaneously clusters users and items
- Good for discovering patterns
- Moderate model size (~3 MB)
- Useful for exploratory analysis

**Implementation**: `surprise.CoClustering()`

## Model Training

### Training Script
Location: `models/train_and_save_models.py`

### Training Process
1. Load ratings data from CSV
2. Create Surprise Dataset object
3. Split into train/test (80/20)
4. Train each algorithm on training set
5. Serialize models using pickle
6. Save to `models/` directory

### Running Training
```bash
cd models
python train_and_save_models.py
```

### Output
```
Training SVD...
Saved SVD to models/SVD.pkl
Training KNN Basic...
Computing the cosine similarity matrix...
Done computing similarity matrix.
Saved KNN Basic to models/KNN Basic.pkl
...
```

## Performance Metrics

### Evaluation Methodology
- **Cross-validation**: 5-fold CV
- **Metrics**: RMSE, MAE, Precision@5, Recall@5
- **Relevance Threshold**: 4.0 stars
- **Evaluation Script**: `Model_Losses.ipynb`

### Model Performance Summary

| Model         | Avg RMSE | Avg MAE | Precision@5 | Recall@5 |
|---------------|----------|---------|-------------|----------|
| SVD           | 0.8736   | 0.6715  | 0.5899      | 0.5727   |
| KNN User      | 0.9721   | 0.7490  | 0.6590      | 0.6772   |
| KNN Item      | 0.9757   | 0.7602  | 0.3163      | 0.3635   |
| Slope One     | 0.9015   | 0.6888  | 0.6147      | 0.6371   |
| BaselineOnly  | 0.8720   | 0.6723  | 0.5514      | 0.5027   |
| CoClustering  | 0.9457   | 0.7323  | 0.5804      | 0.6142   |

### Metric Definitions

**RMSE (Root Mean Square Error)**
- Measures average prediction error
- Lower is better
- Penalizes large errors more than MAE

**MAE (Mean Absolute Error)**
- Average absolute difference between predicted and actual ratings
- Lower is better
- More robust to outliers than RMSE

**Precision@K**
- Proportion of recommended items that are relevant
- Formula: `(# relevant recommended) / (# recommended)`
- Higher is better

**Recall@K**
- Proportion of relevant items that were recommended
- Formula: `(# relevant recommended) / (# total relevant)`
- Higher is better

### Best Algorithm Selection

**For Accuracy (RMSE/MAE)**:
- Best: **BaselineOnly** (RMSE: 0.8720)
- Runner-up: **SVD** (RMSE: 0.8736)

**For Relevance (Precision/Recall)**:
- Best: **KNN User** (Precision: 0.6590, Recall: 0.6772)
- Runner-up: **Slope One** (Precision: 0.6147, Recall: 0.6371)

**Overall Recommendation**: **SVD** - Best balance of accuracy, performance, and model size

## Development

### Backend Development

#### File: `backend/app.py`
Flask API server with single endpoint `/recommend`

Key functions:
- `recommend()`: Handles GET requests, validates parameters, returns recommendations

#### File: `backend/recommender.py`
Recommendation engine and model management

Key components:
- `models`: Dictionary of loaded models
- `get_recommendations(user_id, model, top_n)`: Generates recommendations

#### Adding a New Algorithm
1. Import algorithm from `surprise`
2. Add to `models` dict in `train_and_save_models.py`
3. Train and save model
4. Add option to frontend dropdown in `App.js`

### Frontend Development

#### File: `frontend/src/App.js`
Main React component with state management

State variables:
- `userId`: User input for ID
- `algo`: Selected algorithm
- `movies`: Recommendation results
- `error`: Error message display

#### Customizing UI
- Modify styling in `App.css`
- Update layout in `App.js` return statement
- Add features (e.g., rating display, movie posters, filters)

### Adding Features

#### Example: Add Movie Genres to Results
1. Modify `backend/recommender.py`:
```python
return top_movies[['movieId', 'title', 'genres']].to_dict(orient='records')
```

2. Update `frontend/src/App.js`:
```jsx
<li key={movie.movieId}>
  {movie.title} - {movie.genres}
</li>
```

## References

### Libraries & Frameworks
- [Surprise Documentation](http://surpriselib.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Dataset
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)

---


**Last Updated**: 2025-11-28
**Version**: 1.0.0
**Author**: Ronald Wee
