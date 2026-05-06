import axios from 'axios';

const API_BASE_URL =
  process.env.REACT_APP_API_URL || 'https://campus-placement-api-m9ou.onrender.com/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // Render cold-starts can be slow
});

export const predictionAPI = {
  predictPlacement: (data) => api.post('/predictions/predict/', data),
  getPredictions: () => api.get('/predictions/'),
  getStats: () => api.get('/predictions/stats/'),
  getHealth: () => api.get('/health/'),
};

export default api;
