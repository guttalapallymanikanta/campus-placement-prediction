"""
Model training module for campus placement prediction
"""

import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, cross_val_score
from pathlib import Path
from config import MODEL_SAVE_PATH, RANDOM_STATE


class PlacementModel:
    """Wrapper class for placement prediction models"""
    
    def __init__(self, model_type="random_forest", random_state=RANDOM_STATE):
        """Initialize model based on type"""
        self.model_type = model_type
        self.random_state = random_state
        self.model = self._create_model()
        self.is_trained = False
    
    def _create_model(self):
        """Create model instance based on type"""
        models = {
            "logistic": LogisticRegression(random_state=self.random_state, max_iter=1000),
            "random_forest": RandomForestClassifier(
                n_estimators=100,
                random_state=self.random_state,
                n_jobs=-1
            ),
            "gradient_boost": GradientBoostingClassifier(
                n_estimators=100,
                random_state=self.random_state
            ),
            "svm": SVC(kernel="rbf", random_state=self.random_state, probability=True),
        }
        
        if self.model_type not in models:
            raise ValueError(f"Unknown model type: {self.model_type}")
        
        print(f"Created {self.model_type} model")
        return models[self.model_type]
    
    def train(self, X_train, y_train, validation_split=0.2):
        """Train the model"""
        print(f"\nTraining {self.model_type} model...")
        print(f"Training data shape: {X_train.shape}")
        
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        # Calculate training accuracy
        train_score = self.model.score(X_train, y_train)
        print(f"Training accuracy: {train_score:.4f}")
        
        return train_score
    
    def predict(self, X_test):
        """Make predictions on test data"""
        if not self.is_trained:
            raise RuntimeError("Model must be trained before making predictions")
        
        predictions = self.model.predict(X_test)
        return predictions
    
    def predict_proba(self, X_test):
        """Get prediction probabilities"""
        if not self.is_trained:
            raise RuntimeError("Model must be trained before making predictions")
        
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X_test)
        else:
            raise NotImplementedError(f"{self.model_type} doesn't support probability predictions")
    
    def cross_validate(self, X_train, y_train, cv=5):
        """Perform cross-validation"""
        print(f"\nPerforming {cv}-fold cross-validation...")
        scores = cross_val_score(self.model, X_train, y_train, cv=cv, scoring="accuracy")
        print(f"CV Scores: {scores}")
        print(f"Mean CV Score: {scores.mean():.4f} (+/- {scores.std():.4f})")
        return scores
    
    def get_feature_importance(self, feature_names):
        """Get feature importances (for tree-based models)"""
        if not hasattr(self.model, "feature_importances_"):
            print(f"Feature importance not available for {self.model_type}")
            return None
        
        importance = self.model.feature_importances_
        feature_importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': importance
        }).sort_values('importance', ascending=False)
        
        return feature_importance_df
    
    def save_model(self, filepath=MODEL_SAVE_PATH):
        """Save model to disk"""
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath=MODEL_SAVE_PATH):
        """Load model from disk"""
        with open(filepath, 'rb') as f:
            self.model = pickle.load(f)
        self.is_trained = True
        print(f"Model loaded from {filepath}")


def train_multiple_models(X_train, y_train, X_val=None, y_val=None):
    """Train multiple models and compare performance"""
    model_types = ["logistic", "random_forest", "gradient_boost", "svm"]
    results = {}
    
    for model_type in model_types:
        try:
            print(f"\n{'='*50}")
            model = PlacementModel(model_type=model_type)
            train_score = model.train(X_train, y_train)
            
            if X_val is not None and y_val is not None:
                val_score = model.model.score(X_val, y_val)
                results[model_type] = {
                    'model': model,
                    'train_score': train_score,
                    'val_score': val_score
                }
                print(f"Validation accuracy: {val_score:.4f}")
            else:
                results[model_type] = {
                    'model': model,
                    'train_score': train_score,
                    'val_score': None
                }
        except Exception as e:
            print(f"Error training {model_type}: {e}")
    
    # Print comparison
    print(f"\n{'='*50}")
    print("Model Comparison:")
    for model_type, result in results.items():
        print(f"{model_type}: Train={result['train_score']:.4f}, Val={result['val_score']:.4f}")
    
    return results


if __name__ == "__main__":
    import pandas as pd
    print("Model training module loaded successfully")
