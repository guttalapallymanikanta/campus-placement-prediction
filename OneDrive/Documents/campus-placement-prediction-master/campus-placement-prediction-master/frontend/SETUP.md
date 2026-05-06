# Frontend Setup Guide

## Installation

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend will run at: `http://localhost:3000`

## Project Structure

```
frontend/
├── public/
│   └── index.html           # Main HTML file
├── src/
│   ├── components/
│   │   ├── PredictionForm.js       # Student input form
│   │   ├── PredictionForm.css
│   │   ├── ResultsDisplay.js       # Results table & stats
│   │   └── ResultsDisplay.css
│   ├── App.js              # Main app component
│   ├── App.css
│   ├── index.js            # React entry point
│   ├── index.css
│   └── api.js              # API client
├── package.json
└── SETUP.md               # This file
```

## Features

### Prediction Form
- Student personal information (name, email)
- Academic scores (10th, 12th, degree)
- Degree and specialization selection
- MBA percentage and specialization
- CGPA and salary information

### Results Display
- Statistics dashboard (total, placed, not placed, rate)
- Results table with all predictions
- Confidence percentage for each prediction
- Color-coded placement status

## Available Scripts

```bash
# Start development server
npm start

# Build production bundle
npm build

# Run tests
npm test
```

## Configuration

API endpoint is configured in `src/api.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000/api';
```

Update this if your Django server runs on a different port.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

**Backend not connecting:**
1. Ensure Django server is running on `http://localhost:8000`
2. Check CORS settings in Django settings.py
3. Verify API endpoint in `src/api.js`

**Port 3000 already in use:**
```bash
npm start -- --port 3001
```

**Dependencies issues:**
```bash
rm -rf node_modules package-lock.json
npm install
```

## Building for Production

```bash
npm run build
```

This creates an optimized build in the `build/` folder.
