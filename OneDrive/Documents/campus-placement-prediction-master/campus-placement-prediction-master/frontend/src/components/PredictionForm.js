import React, { useState } from 'react';
import { predictionAPI } from '../api';

/* ─── field definitions ─────────────────────────────────────────────────────── */
const INITIAL = {
  name: '', email: '',
  tenth_score: '', twelfth_score: '',
  degree_percentage: '', cgpa: '',
  degree: 'B.Tech', specialization: 'Mkt&Fin',
  gender: 'M', ssc_b: 'Central', hsc_b: 'Central',
  hsc_s: 'Commerce', workex: 'No',
  salary: '0',
};

const PredictionForm = ({ onPredictionSuccess, disabled }) => {
  const [form, setForm]       = useState(INITIAL);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState(null);
  const [result, setResult]   = useState(null); // holds last prediction result

  const handle = (e) => {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const payload = {
        ...form,
        tenth_score:        parseFloat(form.tenth_score),
        twelfth_score:      parseFloat(form.twelfth_score),
        degree_percentage:  parseFloat(form.degree_percentage),
        cgpa:               parseFloat(form.cgpa),
        salary:             parseFloat(form.salary),
      };

      const res = await predictionAPI.predictPlacement(payload);
      const data = res.data.data;
      setResult(data);
      onPredictionSuccess(data);
      setForm(INITIAL);
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Something went wrong.');
    } finally {
      setLoading(false);
    }
  };

  const placed = result?.prediction === 1;

  return (
    <div className="card">
      <div className="card-title">📋 Student Profile</div>
      <div className="card-subtitle">Fill in your academic details to get a prediction</div>

      {/* ── Inline result card ── */}
      {result && (
        <div className={`result-card ${placed ? 'placed' : 'not-placed'}`}>
          <div className="result-emoji">{placed ? '🎉' : '📚'}</div>
          <div className="result-status">{placed ? 'PLACED!' : 'NOT PLACED'}</div>
          <div className="result-confidence">
            Confidence: <strong>{(result.confidence * 100).toFixed(1)}%</strong>
          </div>
        </div>
      )}

      {error && (
        <div className="alert alert-error">
          <span>❌</span> {error}
        </div>
      )}

      <form onSubmit={handleSubmit} id="prediction-form">

        {/* ── Personal ── */}
        <div className="form-section-label">Personal Info</div>
        <div className="form-grid">
          <div className="field">
            <label htmlFor="name">Full Name *</label>
            <input id="name" name="name" type="text" placeholder="e.g. Arjun Sharma"
              value={form.name} onChange={handle} required />
          </div>
          <div className="field">
            <label htmlFor="email">Email *</label>
            <input id="email" name="email" type="email" placeholder="you@example.com"
              value={form.email} onChange={handle} required />
          </div>
          <div className="field">
            <label htmlFor="gender">Gender</label>
            <select id="gender" name="gender" value={form.gender} onChange={handle}>
              <option value="M">Male</option>
              <option value="F">Female</option>
            </select>
          </div>
          <div className="field">
            <label htmlFor="workex">Work Experience</label>
            <select id="workex" name="workex" value={form.workex} onChange={handle}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </div>
        </div>

        {/* ── Academics ── */}
        <div className="form-section-label">Academic Scores</div>
        <div className="form-grid">
          <div className="field">
            <label htmlFor="tenth_score">10th Score (%) *</label>
            <input id="tenth_score" name="tenth_score" type="number"
              placeholder="0 – 100" min="0" max="100" step="0.01"
              value={form.tenth_score} onChange={handle} required />
          </div>
          <div className="field">
            <label htmlFor="twelfth_score">12th Score (%) *</label>
            <input id="twelfth_score" name="twelfth_score" type="number"
              placeholder="0 – 100" min="0" max="100" step="0.01"
              value={form.twelfth_score} onChange={handle} required />
          </div>
          <div className="field">
            <label htmlFor="degree_percentage">Degree % *</label>
            <input id="degree_percentage" name="degree_percentage" type="number"
              placeholder="0 – 100" min="0" max="100" step="0.01"
              value={form.degree_percentage} onChange={handle} required />
          </div>
          <div className="field">
            <label htmlFor="cgpa">CGPA *</label>
            <input id="cgpa" name="cgpa" type="number"
              placeholder="0.0 – 10.0" min="0" max="10" step="0.01"
              value={form.cgpa} onChange={handle} required />
          </div>
        </div>

        {/* ── Degree ── */}
        <div className="form-section-label">Degree Details</div>
        <div className="form-grid">
          <div className="field">
            <label htmlFor="degree">Degree</label>
            <select id="degree" name="degree" value={form.degree} onChange={handle}>
              <option value="B.Tech">B.Tech / B.E.</option>
              <option value="B.Sc">B.Sc</option>
              <option value="B.Com">B.Com / B.A.</option>
              <option value="Sci&Tech">Sci &amp; Tech</option>
              <option value="Comm&Mgmt">Commerce &amp; Mgmt</option>
              <option value="Others">Others</option>
            </select>
          </div>
          <div className="field">
            <label htmlFor="specialization">Specialisation / MBA</label>
            <select id="specialization" name="specialization" value={form.specialization} onChange={handle}>
              <option value="Mkt&Fin">Mkt &amp; Finance</option>
              <option value="Mkt&HR">Mkt &amp; HR</option>
              <option value="CSE">CSE</option>
              <option value="ECE">ECE</option>
              <option value="Mechanical">Mechanical</option>
              <option value="IT">IT</option>
            </select>
          </div>
          <div className="field">
            <label htmlFor="ssc_b">10th Board</label>
            <select id="ssc_b" name="ssc_b" value={form.ssc_b} onChange={handle}>
              <option value="Central">Central</option>
              <option value="Others">Others</option>
            </select>
          </div>
          <div className="field">
            <label htmlFor="hsc_b">12th Board</label>
            <select id="hsc_b" name="hsc_b" value={form.hsc_b} onChange={handle}>
              <option value="Central">Central</option>
              <option value="Others">Others</option>
            </select>
          </div>
          <div className="field">
            <label htmlFor="hsc_s">12th Stream</label>
            <select id="hsc_s" name="hsc_s" value={form.hsc_s} onChange={handle}>
              <option value="Commerce">Commerce</option>
              <option value="Science">Science</option>
              <option value="Arts">Arts</option>
            </select>
          </div>
          <div className="field">
            <label htmlFor="salary">Expected Salary (₹)</label>
            <input id="salary" name="salary" type="number"
              placeholder="e.g. 500000" min="0" step="10000"
              value={form.salary} onChange={handle} />
          </div>
        </div>

        <button
          type="submit"
          className={`submit-btn${loading ? ' loading' : ''}`}
          disabled={loading || disabled}
        >
          {loading ? (
            <><span className="spinner" />Predicting…</>
          ) : (
            '⚡ Predict My Placement'
          )}
        </button>
      </form>
    </div>
  );
};

export default PredictionForm;
