"""
Main training pipeline for campus placement prediction
Usage: python train.py
"""

import sys
import pandas as pd
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import TRAIN_DATA_PATH, TEST_DATA_PATH
from data_processing import (
    load_data,
    explore_data,
    preprocess_data,
    scale_features,
    split_data,
)
from model_training import PlacementModel, train_multiple_models
from evaluation import evaluate_model


def main():
    """Main training pipeline"""
    
    print("="*60)
    print("CAMPUS PLACEMENT PREDICTION - TRAINING PIPELINE")
    print("="*60)
    
    # Step 1: Load data
    print("\n[1/5] Loading data...")
    if not TRAIN_DATA_PATH.exists():
        print(f"[WARNING] Training data not found at {TRAIN_DATA_PATH}")
        print("Please place your training data at this location:")
        print(f"    {TRAIN_DATA_PATH}")
        print("\nExpected columns: id, placed, [other features]")
        print("\nData format guide:")
        print("  - placed: target variable (0=not placed, 1=placed)")
        print("  - Include relevant features like: 10th_score, 12th_score, degree, salary, etc.")
        return
    
    train_data = load_data(TRAIN_DATA_PATH)
    explore_data(train_data)
    
    # Step 2: Preprocess data
    print("\n[2/5] Preprocessing data...")
    X, y, cat_encoders, target_encoder = preprocess_data(train_data)
    
    # Step 3: Scale features
    print("\n[3/5] Scaling features...")
    X_scaled, scaler = scale_features(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
    
    # Step 4: Split data
    print("\n[4/5] Splitting data...")
    X_train, X_test, y_train, y_test = split_data(X_scaled_df, y)
    
    # Step 5: Train and compare models
    print("\n[5/5] Training models...")
    results = train_multiple_models(X_train, y_train, X_test, y_test)
    
    # Find best model
    best_model_name = max(results, key=lambda x: results[x]['val_score'])
    best_model = results[best_model_name]['model']
    
    print("\n" + "="*60)
    print(f"Best Model: {best_model_name}")
    print("="*60)
    
    # Evaluate best model
    evaluator = evaluate_model(best_model, X_test, y_test)
    evaluator.print_all_evaluations()
    
    # Save best model
    best_model.save_model()
    
    print("\n[DONE] Training pipeline completed!")
    print("Next steps:")
    print("  1. Review the Jupyter notebook for detailed analysis")
    print("  2. Use predict.py to make predictions on new data")


if __name__ == "__main__":
    main()
