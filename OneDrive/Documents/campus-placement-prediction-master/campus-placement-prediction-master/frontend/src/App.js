import React, { useState, useEffect } from 'react';
import PredictionForm from './components/PredictionForm';
import ResultsDisplay from './components/ResultsDisplay';
import './App.css';
import { predictionAPI } from './api';

function App() {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [apiHealth, setApiHealth] = useState(null);

  useEffect(() => {
    checkAPIHealth();
    fetchPredictions();
  }, []);

  const checkAPIHealth = async () => {
    try {
      const response = await predictionAPI.getHealth();
      setApiHealth(response.data);
    } catch (error) {
      console.error('API health check failed:', error);
      setApiHealth({ status: 'unhealthy' });
    }
  };

  const fetchPredictions = async () => {
    try {
      setLoading(true);
      const response = await predictionAPI.getPredictions();
      setPredictions(response.data.results || []);
    } catch (error) {
      console.error('Error fetching predictions:', error);
    } finally {
      setLoading(false);
    }
  };

  const handlePredictionSuccess = (newPrediction) => {
    setPredictions([...predictions, newPrediction]);
  };

  return (
    <div className="App">
      <header className="app-header">
        <h1>🎓 Campus Placement Prediction System</h1>
        <p>Using Machine Learning to predict student placements</p>
        {apiHealth && (
          <div className={`api-status ${apiHealth.status}`}>
            Backend Status: <strong>{apiHealth.status.toUpperCase()}</strong>
          </div>
        )}
      </header>

      <main className="app-main">
        {apiHealth?.status === 'healthy' ? (
          <>
            <PredictionForm onPredictionSuccess={handlePredictionSuccess} />
            {!loading && <ResultsDisplay predictions={predictions} />}
          </>
        ) : (
          <div className="error-banner">
            ⚠️ Backend server is not running! Start the Django server with: python manage.py runserver
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>© 2024 Campus Placement Prediction System. Built with React + Django + Machine Learning.</p>
      </footer>
    </div>
  );
}

export default App;
