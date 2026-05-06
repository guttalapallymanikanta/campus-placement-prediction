"""
Prediction module for campus placement
Usage: python predict.py --input <path_to_data>
"""

import sys
import pandas as pd
import pickle
import numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler, LabelEncoder

sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import MODEL_SAVE_PATH


def load_model_and_scalers(model_path=MODEL_SAVE_PATH):
    """Load trained model and preprocessing components"""
    
    if not Path(model_path).exists():
        raise FileNotFoundError(f"Trained model not found at {model_path}")
    
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    print(f"✅ Model loaded from {model_path}")
    return model


def predict_placement(data, model):
    """Make placement predictions"""
    
    # Create a copy
    data = data.copy()
    
    # Drop non-predictive columns
    cols_to_drop = [col for col in data.columns if col in ['id', 'Unnamed: 0', 'idx']]
    X = data.drop(columns=cols_to_drop, errors='ignore')
    
    # Encode categorical features
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
    
    # Scale features (use same scaling as training)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Make predictions
    predictions = model.predict(X_scaled)
    probabilities = model.predict_proba(X_scaled) if hasattr(model, 'predict_proba') else None
    
    # Create results dataframe
    results = pd.DataFrame({
        'Prediction': predictions,
        'Placement': ['Placed' if p == 1 else 'Not Placed' for p in predictions]
    })
    
    if probabilities is not None:
        results['Probability_Not_Placed'] = probabilities[:, 0]
        results['Probability_Placed'] = probabilities[:, 1]
    
    return results


def main():
    """Main prediction pipeline"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description='Make placement predictions')
    parser.add_argument('--input', required=True, help='Path to input CSV file')
    parser.add_argument('--output', help='Path to save results (optional)')
    
    args = parser.parse_args()
    
    # Load data
    print(f"Loading data from {args.input}")
    data = pd.read_csv(args.input)
    print(f"Loaded {len(data)} records")
    
    # Load model
    print("\nLoading trained model...")
    model = load_model_and_scalers()
    
    # Make predictions
    print("Making predictions...")
    results = predict_placement(data, model)
    
    # Display results
    print("\n" + "="*60)
    print("PREDICTIONS")
    print("="*60)
    print(results.head(10))
    print(f"\nTotal predictions: {len(results)}")
    print(f"Placed: {(results['Placement'] == 'Placed').sum()}")
    print(f"Not Placed: {(results['Placement'] == 'Not Placed').sum()}")
    
    # Save results if output path provided
    if args.output:
        results.to_csv(args.output, index=False)
        print(f"\n✅ Results saved to {args.output}")


if __name__ == "__main__":
    main()
