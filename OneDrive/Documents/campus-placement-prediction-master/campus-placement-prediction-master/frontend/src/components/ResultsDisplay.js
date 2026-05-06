import React, { useState, useEffect } from 'react';
import './ResultsDisplay.css';

const ResultsDisplay = ({ predictions }) => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    if (predictions && predictions.length > 0) {
      const placed = predictions.filter(p => p.prediction === 1).length;
      const total = predictions.length;
      setStats({
        total,
        placed,
        notPlaced: total - placed,
        placementRate: ((placed / total) * 100).toFixed(2)
      });
    }
  }, [predictions]);

  if (!predictions || predictions.length === 0) {
    return (
      <div className="results-display">
        <p className="empty-state">No predictions yet. Submit the form to get started!</p>
      </div>
    );
  }

  return (
    <div className="results-display">
      <h2>Prediction Results</h2>

      {stats && (
        <div className="stats-container">
          <div className="stat-card">
            <div className="stat-number">{stats.total}</div>
            <div className="stat-label">Total Predictions</div>
          </div>
          <div className="stat-card placed">
            <div className="stat-number">{stats.placed}</div>
            <div className="stat-label">Placed</div>
          </div>
          <div className="stat-card not-placed">
            <div className="stat-number">{stats.notPlaced}</div>
            <div className="stat-label">Not Placed</div>
          </div>
          <div className="stat-card rate">
            <div className="stat-number">{stats.placementRate}%</div>
            <div className="stat-label">Placement Rate</div>
          </div>
        </div>
      )}

      <table className="results-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>CGPA</th>
            <th>Prediction</th>
            <th>Confidence</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {predictions.slice().reverse().map((pred, index) => (
            <tr key={index} className={pred.prediction === 1 ? 'placed-row' : 'not-placed-row'}>
              <td>{pred.name}</td>
              <td>{pred.email}</td>
              <td>{pred.cgpa}</td>
              <td>
                <span className={`badge ${pred.prediction === 1 ? 'badge-placed' : 'badge-not-placed'}`}>
                  {pred.prediction === 1 ? 'PLACED' : 'NOT PLACED'}
                </span>
              </td>
              <td>{(pred.confidence * 100).toFixed(2)}%</td>
              <td>{new Date(pred.created_at).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ResultsDisplay;
