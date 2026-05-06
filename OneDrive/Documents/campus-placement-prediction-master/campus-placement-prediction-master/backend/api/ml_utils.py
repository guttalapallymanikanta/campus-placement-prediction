import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from django.conf import settings
from django.core.management.base import BaseCommand
from pathlib import Path


class MLModel:
    """Machine Learning Model Handler"""
    
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.load_model()
    
    def load_model(self):
        """Load trained model"""
        model_path = settings.ML_MODEL_PATH
        
        if not Path(model_path).exists():
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
            print(f"✅ Model loaded from {model_path}")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def predict(self, data_dict):
        """
        Make prediction on input data
        
        Args:
            data_dict: Dictionary with student features
            
        Returns:
            dict with prediction and confidence
        """
        try:
            # Create DataFrame from input
            df = pd.DataFrame([data_dict])
            
            # Select feature columns (exclude personal info)
            feature_columns = [
                'tenth_score', 'twelfth_score', 'degree_percentage',
                'cgpa', 'salary'
            ]
            
            # Create feature DataFrame
            X = pd.DataFrame()
            X['10th_score'] = df['tenth_score']
            X['12th_score'] = df['twelfth_score'] 
            X['degree_p'] = df['degree_percentage']
            X['cgpa'] = df['cgpa']
            X['salary'] = df['salary']
            
            # Encode categorical features
            X['degree'] = df['degree'].map({'B.Tech': 0, 'B.Sc': 1, 'B.Com': 2}).fillna(0)
            X['specialization'] = df['specialization'].map({
                'CSE': 0, 'ECE': 1, 'Mechanical': 2, 'Civil': 3
            }).fillna(4)  # Other
            
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            # Make prediction
            prediction = self.model.predict(X_scaled)[0]
            
            # Get probability
            if hasattr(self.model, 'predict_proba'):
                proba = self.model.predict_proba(X_scaled)[0]
                confidence = float(max(proba))
            else:
                confidence = 1.0
            
            return {
                'prediction': int(prediction),
                'confidence': round(confidence, 4),
                'status': 'Placed' if prediction == 1 else 'Not Placed'
            }
        
        except Exception as e:
            print(f"❌ Error making prediction: {e}")
            raise


# Global model instance
ml_model = None


def get_ml_model():
    """Get or create ML model instance"""
    global ml_model
    if ml_model is None:
        ml_model = MLModel()
    return ml_model
