import React, { useState } from 'react';
import './PredictionForm.css';
import { predictionAPI } from '../api';

const PredictionForm = ({ onPredictionSuccess }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    tenth_score: '',
    twelfth_score: '',
    degree: 'B.Tech',
    specialization: 'CSE',
    degree_percentage: '',
    cgpa: '',
    salary: '0',
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(null);

    try {
      // Convert string values to numbers
      const submitData = {
        ...formData,
        tenth_score: parseFloat(formData.tenth_score),
        twelfth_score: parseFloat(formData.twelfth_score),
        degree_percentage: parseFloat(formData.degree_percentage),
        cgpa: parseFloat(formData.cgpa),
        salary: parseFloat(formData.salary),
      };

      const response = await predictionAPI.predictPlacement(submitData);
      
      setSuccess(`✅ Prediction successful! Status: ${response.data.data.prediction === 1 ? 'PLACED' : 'NOT PLACED'}`);
      onPredictionSuccess(response.data.data);
      
      // Reset form
      setFormData({
        name: '',
        email: '',
        tenth_score: '',
        twelfth_score: '',
        degree: 'B.Tech',
        specialization: 'CSE',
        degree_percentage: '',
        mba_percentage: '',
        mba_specialization: 'IT',
        cgpa: '',
        salary: '0',
      });
    } catch (err) {
      setError(`❌ Error: ${err.response?.data?.error || err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="prediction-form">
      <h2>Campus Placement Prediction</h2>
      
      {error && <div className="alert alert-error">{error}</div>}
      {success && <div className="alert alert-success">{success}</div>}

      <form onSubmit={handleSubmit}>
        <div className="form-section">
          <h3>Personal Information</h3>
          
          <input
            type="text"
            name="name"
            placeholder="Full Name *"
            value={formData.name}
            onChange={handleChange}
            required
          />
          
          <input
            type="email"
            name="email"
            placeholder="Email *"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-section">
          <h3>Academic Scores</h3>
          
          <input
            type="number"
            name="tenth_score"
            placeholder="10th Score (0-100) *"
            min="0"
            max="100"
            step="0.1"
            value={formData.tenth_score}
            onChange={handleChange}
            required
          />
          
          <input
            type="number"
            name="twelfth_score"
            placeholder="12th Score (0-100) *"
            min="0"
            max="100"
            step="0.1"
            value={formData.twelfth_score}
            onChange={handleChange}
            required
          />
          
          <input
            type="number"
            name="degree_percentage"
            placeholder="Degree Percentage (0-100) *"
            min="0"
            max="100"
            step="0.1"
            value={formData.degree_percentage}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-section">
          <h3>Degree Information</h3>
          
          <select name="degree" value={formData.degree} onChange={handleChange}>
            <option value="B.Tech">B.Tech</option>
            <option value="B.Sc">B.Sc</option>
            <option value="B.Com">B.Com</option>
          </select>
          
          <select name="specialization" value={formData.specialization} onChange={handleChange}>
            <option value="CSE">Computer Science (CSE)</option>
            <option value="ECE">Electronics (ECE)</option>
            <option value="Mechanical">Mechanical</option>
            <option value="Civil">Civil</option>
          </select>
        </div>

        <div className="form-section">
          <h3>Additional Information</h3>
          
          <input
            type="number"
            name="cgpa"
            placeholder="CGPA (0-10) *"
            min="0"
            max="10"
            step="0.1"
            value={formData.cgpa}
            onChange={handleChange}
            required
          />
          
          <input
            type="number"
            name="salary"
            placeholder="Salary Offered (₹)"
            min="0"
            step="10000"
            value={formData.salary}
            onChange={handleChange}
          />
        </div>

        <button type="submit" disabled={loading} className="submit-btn">
          {loading ? 'Predicting...' : 'Predict Placement'}
        </button>
      </form>
    </div>
  );
};

export default PredictionForm;
