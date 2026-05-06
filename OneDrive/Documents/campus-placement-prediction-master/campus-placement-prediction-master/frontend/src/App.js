import React, { useState, useEffect } from 'react';
import PredictionForm from './components/PredictionForm';
import ResultsDisplay from './components/ResultsDisplay';
import './App.css';
import { predictionAPI } from './api';

function App() {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [apiHealth, setApiHealth] = useState(null); // null = checking, object = result

  useEffect(() => {
    checkAPIHealth();
    fetchPredictions();
  }, []);

  const checkAPIHealth = async () => {
    try {
      const response = await predictionAPI.getHealth();
      setApiHealth(response.data);
    } catch {
      setApiHealth({ status: 'unhealthy' });
    }
  };

  const fetchPredictions = async () => {
    try {
      setLoading(true);
      const response = await predictionAPI.getPredictions();
      setPredictions(response.data.results || response.data || []);
    } catch {
      // silently fail — predictions table will be empty
    } finally {
      setLoading(false);
    }
  };

  const handlePredictionSuccess = (newPrediction) => {
    setPredictions(prev => [newPrediction, ...prev]);
  };

  /* ── status pill ── */
  let statusClass = 'checking';
  let statusText  = '● Connecting…';
  if (apiHealth !== null) {
    statusClass = apiHealth.status === 'healthy' ? 'healthy' : 'unhealthy';
    statusText  = apiHealth.status === 'healthy' ? 'API Online' : 'API Offline';
  }

  const isReady = apiHealth?.status === 'healthy';

  return (
    <div className="app">
      {/* ── Nav ── */}
      <nav className="nav">
        <div className="nav-brand">
          <span className="nav-brand-icon">🎓</span>
          PlacePredict AI
        </div>
        <div className={`nav-status ${statusClass}`}>
          <div className="pulse-dot" />
          {statusText}
        </div>
      </nav>

      {/* ── Hero ── */}
      <section className="hero">
        <div className="hero-badge">🤖 Machine Learning Powered</div>
        <h1>Campus Placement<br />Prediction System</h1>
        <p className="hero-sub">
          Enter your academic profile and let our ML model predict your
          campus placement outcome with confidence scores.
        </p>
      </section>

      {/* ── Main ── */}
      <main className="main-content">
        {!isReady && apiHealth !== null && (
          <div className="offline-banner">
            <span className="icon">⚠️</span>
            <div>
              <strong>Backend Offline</strong>
              <p>
                The Django API is unreachable. If running locally, start it with:{' '}
                <code>python manage.py runserver</code>
              </p>
            </div>
          </div>
        )}

        <div className="columns">
          <PredictionForm
            onPredictionSuccess={handlePredictionSuccess}
            disabled={!isReady}
          />
          {!loading && <ResultsDisplay predictions={predictions} />}
        </div>
      </main>

      {/* ── Footer ── */}
      <footer className="footer">
        © {new Date().getFullYear()} PlacePredict AI &bull; Built with React + Django + Scikit-Learn &bull; Deployed on Render
      </footer>
    </div>
  );
}

export default App;
