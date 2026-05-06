import React, { useMemo } from 'react';

const ResultsDisplay = ({ predictions }) => {
  const stats = useMemo(() => {
    if (!predictions || predictions.length === 0) return null;
    const total = predictions.length;
    const placed = predictions.filter(p => p.prediction === 1).length;
    return {
      total,
      placed,
      notPlaced: total - placed,
      rate: ((placed / total) * 100).toFixed(1),
    };
  }, [predictions]);

  return (
    <div className="card">
      <div className="card-title">📊 Prediction History</div>
      <div className="card-subtitle">Results from the current session</div>

      {/* Stats tiles */}
      {stats && (
        <div className="stats-row">
          <div className="stat-tile total">
            <div className="num">{stats.total}</div>
            <div className="lbl">Total</div>
          </div>
          <div className="stat-tile placed">
            <div className="num">{stats.placed}</div>
            <div className="lbl">Placed</div>
          </div>
          <div className="stat-tile np">
            <div className="num">{stats.notPlaced}</div>
            <div className="lbl">Not Placed</div>
          </div>
          <div className="stat-tile rate">
            <div className="num">{stats.rate}%</div>
            <div className="lbl">Success Rate</div>
          </div>
        </div>
      )}

      {/* Table */}
      {!predictions || predictions.length === 0 ? (
        <div className="empty-state">
          <div className="icon">🔍</div>
          <p>No predictions yet.<br />Submit the form to get started!</p>
        </div>
      ) : (
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>CGPA</th>
                <th>Degree %</th>
                <th>Result</th>
                <th>Confidence</th>
              </tr>
            </thead>
            <tbody>
              {predictions.map((pred, i) => (
                <tr key={pred.id || i}>
                  <td style={{ color: 'var(--text-primary)', fontWeight: 500 }}>{pred.name}</td>
                  <td>{pred.cgpa}</td>
                  <td>{pred.degree_percentage}%</td>
                  <td>
                    <span className={`badge ${pred.prediction === 1 ? 'badge-placed' : 'badge-np'}`}>
                      {pred.prediction === 1 ? 'Placed' : 'Not Placed'}
                    </span>
                  </td>
                  <td>{pred.confidence != null ? `${(pred.confidence * 100).toFixed(1)}%` : '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default ResultsDisplay;
