import os

# config.py
# Project configuration and hyperparameters for ECG anomaly detection and classification.

DATA_DIR = 'data'
DATA_FILENAME = 'ecg.csv'
DATA_PATH = os.path.join(DATA_DIR, DATA_FILENAME)

KAGGLE_DATASET = 'devavratatripathy/ecg-dataset'
KAGGLE_FILE = 'ecg.csv'

# General settings
RANDOM_STATE = 42
TEST_SIZE_SUPERVISED = 0.2
SMOTE_RANDOM_STATE = 42

# Autoencoder hyperparameters
AE_INPUT_DIM = 140
AE_LATENT_DIM = 16
AE_EPOCHS = 50
AE_BATCH_SIZE = 32
AE_ANOMALY_THRESHOLD_PERCENTILE = 95

# Visualization settings
FIGURE_SIZE_DEFAULT = (12, 6)
FIGURE_SIZE_SMALL = (8, 6)

# Supervised model hyperparameters
RF_N_ESTIMATORS = 100
RF_CLASS_WEIGHT = 'balanced'
RF_HYPER_PARAM_GRID = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}
GBC_N_ESTIMATORS = 100
GBC_LEARNING_RATE = 0.1
GBC_MAX_DEPTH = 3
SVM_KERNEL = 'rbf'
SVM_CLASS_WEIGHT = 'balanced'
