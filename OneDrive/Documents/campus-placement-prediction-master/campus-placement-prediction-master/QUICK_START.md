# ✨ Full Stack Campus Placement Prediction System

Complete web application with Django backend + React frontend + ML model

## 🚀 Quick Start (5 minutes)

### Everything in One Place

```
┌─────────────────────────────────────────────────────────────┐
│                    Browser Frontend                          │
│              React App (http://localhost:3000)              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • Student Form (Name, Email, Scores, etc.)          │   │
│  │ • Real-time Prediction Display                      │   │
│  │ • Results Dashboard with Statistics                 │   │
│  │ • Prediction History Table                          │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────┘
                             │
                      HTTP/CORS Requests
                             │
┌────────────────────────────▼────────────────────────────────┐
│                   Django REST Backend                        │
│              (http://localhost:8000/api)                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ • /api/predictions/predict/ - Make prediction      │   │
│  │ • /api/predictions/ - Get all predictions          │   │
│  │ • /api/predictions/stats/ - Get statistics         │   │
│  │ • /admin/ - Admin panel                            │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
            ┌───────▼───────┐  ┌──────▼──────────────┐
            │   SQLite DB   │  │  ML Model          │
            │ (Predictions) │  │  (scikit-learn)    │
            └───────────────┘  └────────────────────┘
```

## 📋 Pre-Requirements

Before running, make sure:
1. ✅ You have trained the ML model:
   ```bash
   python train.py
   ```
   This creates `models/placement_model.pkl`

2. ✅ Check the model exists:
   ```bash
   ls models/placement_model.pkl
   ```

## 🎯 Step-by-Step Setup

### Step 1: Open Terminal 1 (Backend)

```powershell
cd c:\Users\dhawa\Desktop\campus_placements
cd backend

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Start server
python manage.py runserver
```

✅ **Backend ready at:** `http://localhost:8000`

### Step 2: Open Terminal 2 (Frontend)

```powershell
cd c:\Users\dhawa\Desktop\campus_placements
cd frontend

# Install dependencies
npm install

# Start React app
npm start
```

✅ **Frontend ready at:** `http://localhost:3000`

### Step 3: Open Browser

Go to: **http://localhost:3000**

🎉 **System is running!**

---

## 📝 Using the Application

### Input Form
1. Enter student name and email
2. Fill in academic scores (10th, 12th, degree percentage)
3. Select degree and specialization
4. Enter MBA details (percentage and specialization)
5. Enter CGPA
6. (Optional) Enter offered salary
7. Click **"Predict Placement"**

### Results
- Prediction badge showing **PLACED** or **NOT PLACED**
- Confidence score (e.g., 98% confident)
- All predictions saved to database
- View statistics: Total, Placed, Not Placed, Placement Rate

### Admin Panel
Access at: `http://localhost:8000/admin/`
- Login with superuser credentials
- View all predictions
- Export data

---

## 🔧 API Testing (Optional)

### Using cURL (Power Shell)

```powershell
# Test backend health
curl http://localhost:8000/api/health/

# Make a prediction
curl -X POST http://localhost:8000/api/predictions/predict/ `
  -H "Content-Type: application/json" `
  -d '{
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
  }'
```

---

## 🛑 Troubleshooting

### Issue: "Backend not found"
**Solution:** Ensure Django is running on Terminal 1
```bash
python manage.py runserver
```

### Issue: "npm install fails"
**Solution:** Update npm
```bash
npm install -g npm@latest
npm install
```

### Issue: "Model not loading"
**Solution:** Make sure ML model is trained
```bash
python train.py
```

### Issue: "Port 3000 already in use"
**Solution:** Use different port
```bash
npm start -- --port 3001
```

### Issue: "Port 8000 already in use"
**Solution:** Use different port
```bash
python manage.py runserver 8001
```

### Issue: "Database locked"
**Solution:** Reset database
```bash
python manage.py migrate --run-syncdb
```

---

## 📊 What's Happening Behind the Scenes

1. **Frontend (React)** - User fills form with student data
2. **Network Request** - Form data sent to Django API
3. **Backend (Django)** - Receives request, validates data
4. **ML Model** - Loads trained scikit-learn model
5. **Prediction** - Makes placement prediction
6. **Database** - Saves prediction to SQLite
7. **Response** - Returns result to frontend
8. **UI Update** - Displays result in table and statistics

---

## 🚀 Next: Deployment

To deploy to production:
- See [FULLSTACK_SETUP.md](../FULLSTACK_SETUP. md) for deployment guide
- Use Gunicorn for Django
- Build React for production: `npm run build`
- Deploy to AWS, Heroku, DigitalOcean, etc.

---

## 📚 Documentation

- [Complete Setup Guide](../FULLSTACK_SETUP.md)
- [Backend Docs](./SETUP.md)
- [Frontend Docs](../frontend/SETUP.md)
- [Main README](../README.md)

---

## ✅ Checklist

Before running:
- [ ] Python 3.7+ installed
- [ ] Node.js 14+ installed
- [ ] ML model trained (`python train.py`)
- [ ] Model file exists (`models/placement_model.pkl`)
- [ ] Both requirements.txt files accessible

Terminal 1 (Backend):
- [ ] Virtual environment activated
- [ ] Dependencies installed
- [ ] Database migrated
- [ ] Django server running (port 8000)

Terminal 2 (Frontend):
- [ ] Node modules installed
- [ ] React app running (port 3000)

Browser:
- [ ] Can access http://localhost:3000
- [ ] Form loads without errors
- [ ] Backend status shows "healthy"

---

**Ready to go! 🎉**

Visit http://localhost:3000 and start making predictions!
