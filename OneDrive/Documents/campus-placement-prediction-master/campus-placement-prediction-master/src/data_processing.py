"""
Data loading and preprocessing module for campus placement prediction
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from pathlib import Path
from config import (
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    TARGET_COLUMN,
    DROP_COLUMNS,
    TEST_SIZE,
    RANDOM_STATE,
)


def load_data(filepath):
    """Load data from CSV file"""
    if not Path(filepath).exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    data = pd.read_csv(filepath)
    print(f"Data loaded: {data.shape}")
    print(f"Columns: {list(data.columns)}")
    return data


def explore_data(data):
    """Basic data exploration"""
    print("\n=== Data Info ===")
    print(data.info())
    print("\n=== Data Statistics ===")
    print(data.describe())
    print("\n=== Missing Values ===")
    print(data.isnull().sum())
    print("\n=== Target Distribution ===")
    if TARGET_COLUMN in data.columns:
        print(data[TARGET_COLUMN].value_counts(normalize=True))


def handle_missing_values(data, strategy="mean"):
    """Handle missing values in the dataset"""
    if data.isnull().sum().sum() == 0:
        print("No missing values found")
        return data
    
    print(f"\nHandling missing values using '{strategy}' strategy")
    
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    categorical_cols = data.select_dtypes(include=['object']).columns
    
    # Fill numeric columns with mean
    for col in numeric_cols:
        if data[col].isnull().sum() > 0:
            data[col].fillna(data[col].mean(), inplace=True)
    
    # Fill categorical columns with mode
    for col in categorical_cols:
        if data[col].isnull().sum() > 0:
            data[col].fillna(data[col].mode()[0], inplace=True)
    
    print(f"Missing values after handling: {data.isnull().sum().sum()}")
    return data


def encode_categorical_features(data, categorical_cols=None, fit_encoder=True, encoders=None):
    """Encode categorical features using LabelEncoder"""
    if categorical_cols is None:
        categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
        if TARGET_COLUMN in categorical_cols:
            categorical_cols.remove(TARGET_COLUMN)
    
    if fit_encoder:
        encoders = {}
        print(f"\nEncoding categorical features: {categorical_cols}")
        for col in categorical_cols:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))
            encoders[col] = le
        return data, encoders
    else:
        if encoders is None:
            raise ValueError("Encoders must be provided when fit_encoder=False")
        for col, le in encoders.items():
            if col in data.columns:
                data[col] = le.transform(data[col].astype(str))
        return data, encoders


def encode_target(y, fit_encoder=True, encoder=None):
    """Encode target variable"""
    if fit_encoder:
        le = LabelEncoder()
        y_encoded = le.fit_transform(y)
        return y_encoded, le
    else:
        if encoder is None:
            raise ValueError("Encoder must be provided when fit_encoder=False")
        return encoder.transform(y), encoder


def preprocess_data(data, target_col=TARGET_COLUMN, drop_cols=DROP_COLUMNS, encoders=None):
    """Complete preprocessing pipeline"""
    print("\n=== Data Preprocessing ===")
    
    # Create a copy to avoid modifying original
    data = data.copy()
    
    # Drop unnecessary columns
    for col in drop_cols:
        if col in data.columns:
            data = data.drop(columns=[col])
    
    # Handle missing values
    data = handle_missing_values(data)
    
    # Separate features and target
    X = data.drop(columns=[target_col])
    y = data[target_col]
    
    # Encode categorical features
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    if len(categorical_cols) > 0:
        X, cat_encoders = encode_categorical_features(X, categorical_cols, fit_encoder=(encoders is None), encoders=encoders)
    else:
        cat_encoders = {}
    
    # Encode target
    y_encoded, target_encoder = encode_target(y, fit_encoder=(encoders is None or 'target' not in encoders))
    
    print(f"\nFinal shape - X: {X.shape}, y: {y_encoded.shape}")
    print(f"Features: {list(X.columns)}")
    
    return X, y_encoded, cat_encoders, target_encoder


def scale_features(X_train, X_test=None, fit_scaler=True, scaler=None):
    """Scale numerical features"""
    if fit_scaler:
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        print(f"\nFeatures scaled. Shape: {X_train_scaled.shape}")
        
        if X_test is not None:
            X_test_scaled = scaler.transform(X_test)
            return X_train_scaled, X_test_scaled, scaler
        return X_train_scaled, scaler
    else:
        if scaler is None:
            raise ValueError("Scaler must be provided when fit_scaler=False")
        X_train_scaled = scaler.transform(X_train)
        if X_test is not None:
            X_test_scaled = scaler.transform(X_test)
            return X_train_scaled, X_test_scaled
        return X_train_scaled


def split_data(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE):
    """Split data into train and test sets"""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    print(f"\nData split: Train {X_train.shape}, Test {X_test.shape}")
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    # Example usage
    print("Data processing module loaded successfully")
