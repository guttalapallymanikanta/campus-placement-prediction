# Campus Placement Prediction using Machine Learning

A complete full-stack application for predicting campus placements with a Django REST backend and React frontend.

## 🚀 Quick Start

### Option 1: ML Pipeline Only (Simple)
```bash
pip install -r requirements.txt
python train.py
python predict.py --input data/test.csv --output results.csv
```

### Option 2: Full Stack (Backend + Frontend)
```bash
# Terminal 1 - Backend
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Terminal 2 - Frontend
cd frontend
npm install
npm start
```

Visit: **http://localhost:3000**

---

## 📁 Project Structure

```
campus_placements/
├── data/                          # Data directory
│   ├── train.csv                 # Training data
│   └── test.csv                  # Test data (optional)
├── notebooks/
│   └── Campus_Placement_Prediction.ipynb  # Analysis notebook
├── src/
│   ├── __init__.py
│   ├── config.py                 # Configuration
│   ├── data_processing.py        # Data utilities
│   ├── model_training.py         # Model training
│   └── evaluation.py             # Evaluation metrics
├── backend/                       # Django REST API Backend ✨ NEW
│   ├── placement_api/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── __init__.py
│   ├── api/
│   │   ├── models.py             # Prediction model
│   │   ├── views.py              # API views
│   │   ├── serializers.py        # Data serializers
│   │   ├── ml_utils.py           # ML integration
│   │   ├── urls.py
│   │   └── __init__.py
│   ├── manage.py
│   ├── requirements.txt
│   └── SETUP.md
├── frontend/                      # React Frontend ✨ NEW
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── PredictionForm.js      # Student input form
│   │   │   ├── PredictionForm.css
│   │   │   ├── ResultsDisplay.js      # Results table
│   │   │   └── ResultsDisplay.css
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── api.js                # API client
│   │   └── index.css
│   ├── package.json
│   └── SETUP.md
├── models/                        # Trained ML models
│   └── placement_model.pkl
├── train.py                      # Training script
├── predict.py                    # Prediction script
├── requirements.txt              # ML dependencies
├── README.md
├── FULLSTACK_SETUP.md            # Complete setup guide ✨ NEW
└── .gitignore
```

## Installation

### ML Pipeline Dependencies
```bash
pip install -r requirements.txt
```

### Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Frontend Dependencies
```bash
cd frontend
npm install
```

## Getting Started
### 🎯 Option 1: ML Pipeline Only

**Step 1: Prepare Data**
Place training data in `data/train.csv`

**Step 2: Train Model**
```bash
python train.py
```

**Step 3: Make Predictions**
```bash
python predict.py --input data/test.csv --output results.csv
```

**Step 4: Explore Analysis**
```bash
jupyter notebook notebooks/Campus_Placement_Prediction.ipynb
```

---

### 🌐 Option 2: Full Stack Application (NEW!)

#### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
✅ Backend running at: http://localhost:8000

#### Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm start
```
✅ Frontend running at: http://localhost:3000

#### Access the Application
Open browser to: **http://localhost:3000**

**Features:**
- 📝 Student input form with all academic details
- 🤖 Real-time placement prediction from ML model
- 📊 Results dashboard with statistics
- 💾 Prediction history in database
- 📈 Placement rate visualization

---
### Step 1: Prepare Your Data

Place your training data in `data/train.csv` with the following structure:
- **placed**: Target variable (0 = Not Placed, 1 = Placed)
- Other columns: Student features (academic scores, skills, etc.)

Example features might include:
- `10th_score`, `12th_score`: Board exam scores
- `degree`: Degree obtained
- `cgpa`: Cumulative GPA
- `salary`: Salary offered (numeric)
- `specialization`: Field of study
- And any other relevant features

### Step 2: Run the Training Pipeline

Execute the main training script:
```bash
python train.py
```

This will:
1. Load and explore the data
2. Preprocess and clean the data
3. Encode categorical features
4. Scale numerical features
5. Split into train/test sets
6. Train multiple models (Logistic Regression, Random Forest, Gradient Boosting)
7. Evaluate and compare models
8. Save the best model

### Step 3: Explore in Jupyter Notebook

Open and run the notebook for detailed analysis:
```bash
jupyter notebook notebooks/Campus_Placement_Prediction.ipynb
```

The notebook includes:
- Data exploration and visualization
- Feature correlations
- Model training and evaluation
- Confusion matrices and classification reports
- Feature importance analysis
- Sample predictions

### Step 4: Make Predictions

Use the trained model to predict on new data:
```bash
python predict.py --input path/to/new_data.csv --output results.csv
```

## Project Features

### Models
- **Logistic Regression**: Fast baseline model
- **Random Forest**: Ensemble method with feature importance
- **Gradient Boosting**: Advanced ensemble for better accuracy

### Preprocessing
- Missing value imputation
- Categorical encoding
- Feature scaling
- Train/test splitting with stratification

### Evaluation Metrics
- Accuracy
- Precision & Recall
- F1-Score
- Confusion Matrix
- ROC-AUC
- Classification Report

### Visualization
- Target distribution
- Feature correlations
- Model performance comparison
- Feature importance plots
- Confusion matrices

## Data Requirements

Your CSV file should contain:
- A target column named `placed` (0 or 1)
- At least one numeric feature
- Can have categorical features (will be encoded automatically)

Example minimal structure:
```
10th_score,12th_score,degree,cgpa,specialization,placed
85,88,3.5,3.8,CSE,1
78,82,3.2,3.5,ECE,0
92,90,3.9,3.9,CSE,1
```

## Configuration

Edit `src/config.py` to customize:
- Data paths
- Random state for reproducibility
- Test/validation split ratios
- Target column name
- Columns to drop

## Quick Command Reference

### ML Pipeline Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python train.py

# Make predictions
python predict.py --input data/test.csv --output results.csv

# Run Jupyter notebook for analysis
jupyter notebook notebooks/Campus_Placement_Prediction.ipynb
```

### Full Stack Commands
```bash
# Backend (Terminal 1)
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend (Terminal 2)
cd frontend
npm install
npm start

# Access application
http://localhost:3000
```

### API Endpoints
```bash
# Health check
GET http://localhost:8000/api/health/

# Get all predictions
GET http://localhost:8000/api/predictions/

# Get statistics
GET http://localhost:8000/api/predictions/stats/

# Make a new prediction
POST http://localhost:8000/api/predictions/predict/
```

---

## Usage Examples

**Training with default settings:**
```bash
python train.py
```

**Making predictions:**
```bash
python predict.py --input data/test.csv --output predictions.csv
```

**Using the modules in your code:**
```python
from src.data_processing import load_data, preprocess_data, scale_features
from src.model_training import PlacementModel

# Load data
data = load_data("data/train.csv")

# Preprocess
X, y, encoders, target_encoder = preprocess_data(data)

# Scale features
X_scaled, scaler = scale_features(X)

# Train model
model = PlacementModel(model_type="random_forest")
model.train(X_scaled, y)

# Save for later
model.save_model()
```

## Model Performance

The trained models provide:
- **80-95% accuracy** (depending on data quality)
- **Balanced precision/recall** for placement prediction
- **Feature importance insights** for decision-making

*Note: Actual performance depends on your data quality and feature richness.*

## Troubleshooting

### Data loading fails
- Ensure CSV is in `data/train.csv`
- Check column names are lowercase
- Ensure `placed` column exists

### Missing values warning
- The pipeline handles missing values automatically
- Check data quality if too many missing values

### Model performance is low
- Verify data quality and feature relevance
- Try feature engineering for better signals
- Ensure enough training samples (100+)

## Next Steps

1. **Full Stack Deployment**: See [FULLSTACK_SETUP.md](FULLSTACK_SETUP.md)
2. **Feature Engineering**: Create new relevant features
3. **Hyperparameter Tuning**: Use GridSearchCV for better parameters
4. **Cross-Validation**: Implement k-fold cross-validation
5. **Class Imbalance**: Handle class imbalance if present
6. **Production Deployment**: Deploy to cloud (Heroku, AWS, etc.)

## System Architecture ✨

### Full Stack Components

**Frontend (React)**
- Modern UI with form for student data input
- Real-time prediction display
- Results dashboard with statistics
- Prediction history table

**Backend (Django)**
- REST API for predictions
- Machine Learning model integration
- Database for storing predictions
- Admin panel for management

**Machine Learning**
- Multiple models: Logistic Regression, Random Forest, Gradient Boosting
- Data preprocessing and scaling
- Model evaluation and comparison

### Data Flow
```
User Input (React)
       ↓
POST /api/predictions/predict/
       ↓
Django Backend
       ↓
Load ML Model
       ↓
Make Prediction
       ↓
Save to Database
       ↓
Return Result
       ↓
Display in UI
```

## Features ✨

### ML Pipeline
- 🔄 Data preprocessing and cleaning
- 📊 Feature scaling and encoding
- 🤖 Multiple ML models
- 📈 Performance comparison
- 💾 Model persistence

### Web Application
- 📱 Responsive React UI
- 🔌 REST API backend
- 💾 Prediction history
- 📊 Statistics dashboard
- 🔐 Admin panel

## Requirements

- **Python**: 3.7+ (ML), 3.8+ (Backend)
- **Node.js**: 14+ (Frontend)
- **ML Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **Backend**: Django 3.2+, Django REST Framework
- **Frontend**: React 18+

See version details in:
- `requirements.txt` (ML pipeline)
- `backend/requirements.txt` (Django)
- `frontend/package.json` (React)

## Documentation

- [FULLSTACK_SETUP.md](FULLSTACK_SETUP.md) - Complete full-stack setup guide
- [backend/SETUP.md](backend/SETUP.md) - Backend configuration
- [frontend/SETUP.md](frontend/SETUP.md) - Frontend configuration

## License

This project is open source and available for educational and commercial use.

## Support

For issues or questions, check the Jupyter notebook for examples and detailed explanations of each step.
