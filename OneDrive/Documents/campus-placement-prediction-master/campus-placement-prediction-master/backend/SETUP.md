# Backend Setup Guide

## Installation

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

1. **Database Setup**
```bash
python manage.py makemigrations
python manage.py migrate
```

2. **Create Superuser (Admin)**
```bash
python manage.py createsuperuser
```

## Running the Server

```bash
python manage.py runserver
```

Server will run at: `http://localhost:8000`

## API Endpoints

### Health Check
- **GET** `/api/health/` - Check API status

### Predictions
- **POST** `/api/predictions/predict/` - Make a new prediction
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "tenth_score": 85,
    "twelfth_score": 88,
    "degree": "B.Tech",
    "specialization": "CSE",
    "degree_percentage": 70.5,
    "mba_percentage": 75.2,
    "mba_specialization": "IT",
    "cgpa": 8.5,
    "salary": 650000
  }
  ```

- **GET** `/api/predictions/` - Get all predictions
- **GET** `/api/predictions/stats/` - Get prediction statistics
- **GET** `/api/predictions/{id}/` - Get specific prediction

## Admin Panel

Access admin panel at: `http://localhost:8000/admin/`

Login with your superuser credentials to manage predictions.

## Testing with cURL

```bash
# Test health check
curl http://localhost:8000/api/health/

# Make a prediction
curl -X POST http://localhost:8000/api/predictions/predict/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Student",
    "email": "test@example.com",
    "tenth_score": 85,
    "twelfth_score": 88,
    "degree": "B.Tech",
    "specialization": "CSE",
    "degree_percentage": 70.5,
    "mba_percentage": 75.2,
    "mba_specialization": "IT",
    "cgpa": 8.5,
    "salary": 650000
  }'
```

## Troubleshooting

**Port already in use:**
```bash
python manage.py runserver 8001
```

**Database errors:**
```bash
python manage.py migrate --run-syncdb
```

**Model loading error:**
Ensure your trained model is at: `../models/placement_model.pkl`
