# Full Stack Deployment Guide

## System Requirements

- Python 3.7+
- Node.js 14+
- npm 6+
- Django 3.2+
- React 18+

## Complete Setup Instructions

### Step 1: Prepare ML Model

First, make sure you have trained the model:

```bash
cd c:\Users\dhawa\Desktop\campus_placements
python train.py
```

This creates `models/placement_model.pkl`

### Step 2: Setup Backend

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server on port 8000
python manage.py runserver
```

Backend runs at: **http://localhost:8000**

### Step 3: Setup Frontend

In a separate terminal:

```bash
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

Frontend runs at: **http://localhost:3000**

## Running Both Servers

### Terminal 1 - Backend
```bash
cd backend
venv\Scripts\activate
python manage.py runserver
```

### Terminal 2 - Frontend
```bash
cd frontend
npm start
```

Then visit: **http://localhost:3000**

## API Workflow

```
User fills form (React)
     ↓
Sends POST request to Django API
     ↓
Django loads ML model
     ↓
Predicts placement status
     ↓
Saves to database
     ↓
Returns result to React
     ↓
Displays result in table
```

## Database Models

### Prediction Model
```python
- id: Auto-generated
- name: Student name
- email: Student email
- tenth_score: 10th board score
- twelfth_score: 12th board score
- degree: B.Tech/B.Sc/B.Com
- specialization: CSE/ECE/Mechanical/Civil
- degree_percentage: Degree percentage
- mba_percentage: MBA percentage
- mba_specialization: IT/Finance/Marketing/HR
- cgpa: Cumulative GPA
- salary: Offered salary
- prediction: 0 (Not Placed) or 1 (Placed)
- confidence: Prediction confidence (0-1)
- created_at: Timestamp
```

## API Response Format

### Successful Prediction
```json
{
  "success": true,
  "message": "Student Placed with confidence 0.98",
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "prediction": 1,
    "confidence": 0.98,
    "created_at": "2024-03-06T12:00:00Z"
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message here"
}
```

## CORS Configuration

Django CORS settings allow requests from:
- http://localhost:3000
- http://localhost:8000
- http://127.0.0.1:3000
- http://127.0.0.1:8000

For production, update in `backend/placement_api/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    'https://yourdomain.com',
    'https://www.yourdomain.com',
]
```

## Testing the System

### Test 1: Backend Health Check
```bash
curl http://localhost:8000/api/health/
```

### Test 2: Make Prediction via API
```bash
curl -X POST http://localhost:8000/api/predictions/predict/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@test.com","tenth_score":85,...}'
```

### Test 3: View Frontend
Open browser to http://localhost:3000

## Troubleshooting

### Backend starts but frontend can't connect
- Check Django CORS settings
- Ensure Django is on port 8000
- Check browser console for errors

### Frontend won't start
```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
npm start
```

### Model not loading
- Verify `models/placement_model.pkl` exists
- Check path in `backend/placement_api/settings.py`
- Run `python train.py` if model missing

### Database locked
```bash
python manage.py migrate --run-syncdb
```

## Deployment to Production

### Using Gunicorn + Nginx

```bash
# Install Gunicorn
pip install gunicorn

# Run Gunicorn
gunicorn placement_api.wsgi:application --bind 0.0.0.0:8000

# Build React for production
npm run build
```

Refer to deployment docs for your hosting platform (Heroku, AWS, DigitalOcean, etc.)

## System Architecture

```
┌─────────────────────────────────────┐
│        Browser (React App)           │
│      http://localhost:3000           │
└────────────────┬────────────────────┘
                 │
                 │ HTTP Requests
                 │ (CORS enabled)
                 ↓
┌─────────────────────────────────────┐
│    Django REST API (Backend)         │
│      http://localhost:8000           │
│  - PredictionViewSet                 │
│  - HealthCheckView                   │
└────────────────┬────────────────────┘
                 │
          ┌──────┴──────┐
          ↓             ↓
    ┌─────────┐  ┌────────────┐
    │Database │  │ML Model    │
    │SQLite   │  │(scikit-learn)
    └─────────┘  └────────────┘
```

## Security Notes

For production:
1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a secure value
3. Set proper `ALLOWED_HOSTS`
4. Use environment variables for sensitive settings
5. Enable HTTPS
6. Set up proper database (PostgreSQL)
7. Use a production server (Gunicorn, uWSGI)

## Performance Tips

1. Use caching for model loading
2. Optimize database queries
3. Implement pagination for results
4. Use async tasks for long-running predictions
5. Cache API responses

---

**Questions?** Check the individual SETUP.md files in `backend/` and `frontend/` folders.
