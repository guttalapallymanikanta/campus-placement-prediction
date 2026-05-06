import pickle
import pandas as pd
from django.conf import settings
from pathlib import Path


class MLModel:
    """Machine Learning Model Handler"""

    def __init__(self):
        self.model = None
        self.scaler = None
        self.encoders = {}
        self.feature_columns = []
        self.load_model()

    def load_model(self):
        """Load trained model bundle (model + scaler + encoders + feature columns)"""
        model_path = settings.ML_MODEL_PATH

        if not Path(model_path).exists():
            raise FileNotFoundError(f"Model not found at {model_path}")

        try:
            with open(model_path, 'rb') as f:
                bundle = pickle.load(f)

            # Support both old (raw model) and new (bundle dict) formats
            if isinstance(bundle, dict):
                self.model = bundle['model']
                self.scaler = bundle.get('scaler')
                self.encoders = bundle.get('encoders', {})
                self.feature_columns = bundle.get('feature_columns', [])
            else:
                self.model = bundle

            print(f"[OK] Model loaded from {model_path}")
        except Exception as e:
            print(f"[ERROR] Error loading model: {e}")
            raise

    def predict(self, data_dict):
        """
        Make prediction on input data.
        Feature columns: tenth_score, twelfth_score, degree_percentage, cgpa, salary,
                         gender, ssc_b, hsc_b, hsc_s, degree_t, workex, specialisation
        """
        try:
            row = {
                'tenth_score':       float(data_dict.get('tenth_score', 0)),
                'twelfth_score':     float(data_dict.get('twelfth_score', 0)),
                'degree_percentage': float(data_dict.get('degree_percentage', 0)),
                'cgpa':              float(data_dict.get('cgpa', 0)),
                'salary':            float(data_dict.get('salary', 0)),
                'gender':            str(data_dict.get('gender', 'M')),
                'ssc_b':             str(data_dict.get('ssc_b', 'Central')),
                'hsc_b':             str(data_dict.get('hsc_b', 'Central')),
                'hsc_s':             str(data_dict.get('hsc_s', 'Commerce')),
                'degree_t':          str(data_dict.get('degree', 'Sci&Tech')),
                'workex':            str(data_dict.get('workex', 'No')),
                'specialisation':    str(data_dict.get('specialization', 'Mkt&Fin')),
            }

            df = pd.DataFrame([row])

            # Encode categoricals using saved encoders (or fit fresh if unseen)
            cat_cols = ['gender', 'ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'workex', 'specialisation']
            for col in cat_cols:
                if col in self.encoders:
                    le = self.encoders[col]
                    val = str(df[col].iloc[0])
                    # Handle unseen label gracefully
                    if val in le.classes_:
                        df[col] = le.transform(df[col].astype(str))
                    else:
                        df[col] = 0  # default to first class
                else:
                    from sklearn.preprocessing import LabelEncoder
                    le = LabelEncoder()
                    df[col] = le.fit_transform(df[col].astype(str))

            # Reorder columns to match training order
            if self.feature_columns:
                df = df[self.feature_columns]

            # Scale
            if self.scaler:
                X_scaled = pd.DataFrame(
                    self.scaler.transform(df),
                    columns=self.feature_columns
                )
            else:
                X_scaled = df

            # Predict
            prediction = self.model.predict(X_scaled)[0]

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
            print(f"[ERROR] Error making prediction: {e}")
            raise


# Singleton
ml_model = None


def get_ml_model():
    """Get or create ML model instance"""
    global ml_model
    if ml_model is None:
        ml_model = MLModel()
    return ml_model
