import React, { useState } from 'react';

function App() {
  const [userId, setUserId] = useState('');
  const [algo, setAlgo] = useState('SVD');
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState('');

  const fetchRecommendations = async () => {
    setError('');
    setMovies([]);

    if (!userId) {
      setError('Please enter a user ID.');
      return;
    }

    try {
      const res = await fetch(`/recommend?user_id=${userId}&algo=${encodeURIComponent(algo)}`);
      if (!res.ok) throw new Error(`Server error: ${res.status}`);
      const data = await res.json();
      setMovies(data);
    } catch (err) {
      setError('Failed to fetch recommendations. Please check backend or input.');
      console.error(err);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>🎬 Movie Recommender</h1>

      <div style={{ marginBottom: '1rem' }}>
        <input
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          placeholder="Enter user ID"
          style={{ padding: '0.5rem', marginRight: '1rem' }}
        />

        <select value={algo} onChange={(e) => setAlgo(e.target.value)} style={{ padding: '0.5rem' }}>
          <option value="SVD">SVD</option>
          <option value="KNN Basic">KNN Basic</option>
          <option value="KNN Item">KNN Item</option>
          <option value="Slope One">Slope One</option>
          <option value="BaselineOnly">BaselineOnly</option>
          <option value="CoClustering">CoClustering</option>
        </select>

        <button onClick={fetchRecommendations} style={{ padding: '0.5rem', marginLeft: '1rem' }}>
          Get Recommendations
        </button>
      </div>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {movies.length > 0 ? (
        <ul>
          {movies.map((movie) => (
            <li key={movie.movieId}>{movie.title}</li>
          ))}
        </ul>
      ) : (
        !error && <p>No recommendations yet. Try a different user ID.</p>
      )}
    </div>
  );
}

export default App;
