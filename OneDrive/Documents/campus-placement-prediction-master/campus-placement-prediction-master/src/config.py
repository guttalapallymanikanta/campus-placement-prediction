"""
Configuration settings for campus placement prediction project
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)
NOTEBOOKS_DIR.mkdir(exist_ok=True)

# Data settings
TRAIN_DATA_PATH = DATA_DIR / "train.csv"
TEST_DATA_PATH = DATA_DIR / "test.csv"
MODEL_SAVE_PATH = MODELS_DIR / "placement_model.pkl"

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.1

# Feature settings
TARGET_COLUMN = "placed"
DROP_COLUMNS = ["id", "mba_p", "mba_specialization"]

print(f"Project root: {PROJECT_ROOT}")
print(f"Data directory: {DATA_DIR}")
