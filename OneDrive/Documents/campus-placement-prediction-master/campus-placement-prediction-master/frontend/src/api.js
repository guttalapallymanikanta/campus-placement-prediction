import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const predictionAPI = {
  predictPlacement: (data) => api.post('/predictions/predict/', data),
  getPredictions: () => api.get('/predictions/'),
  getStats: () => api.get('/predictions/stats/'),
  getHealth: () => api.get('/health/'),
};

export default api;
