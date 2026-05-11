# ECG Anomaly Detection and Classification

This repository contains a modular Python implementation for Electrocardiogram (ECG) anomaly detection and classification. The workflow includes data preprocessing, autoencoder-based anomaly detection, supervised classification, and post-hoc misclassification analysis.

## Project Structure

- `config.py` - central project settings, dataset path, Kaggle dataset source, and model hyperparameters.
- `data_preprocessing.py` - dataset download from Kaggle, cleaning, scaling, and SMOTE balancing.
- `autoencoder_model.py` - autoencoder architecture, training, and anomaly detection logic.
- `supervised_models.py` - preparation and training of RandomForest, GradientBoosting, and SVM models.
- `model_evaluation.py` - ROC and Precision-Recall plotting, plus confusion matrix comparison.
- `misclassification_analysis.py` - in-depth analysis of misclassified samples and clustering.
- `utils.py` - plotting utilities for ECG waveforms, label distribution, and confusion matrices.
- `main.py` - executes the full ECG pipeline from preprocessing through evaluation.
- `download_data.py` - downloads the Kaggle ECG dataset to `data/ecg.csv`.
- `requirements.txt` - Python dependencies for the project.
- `data/ecg.csv` - dataset downloaded from Kaggle when you run the workflow.

## Installation

1. Create a Python environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Kaggle Setup

This project downloads the ECG dataset from Kaggle automatically on first run. Configure your Kaggle API credentials by placing a `kaggle.json` file in your home directory under `~/.kaggle/kaggle.json` or by setting the environment variables `KAGGLE_USERNAME` and `KAGGLE_KEY`.

If you already have the dataset locally, the project will use `data/ecg.csv` directly.

## Downloading Data Separately

A dedicated data download script is provided for convenience:

```bash
python download_data.py
```

This will download and extract `ecg.csv` into the `data/` folder.

## Usage

Run the full pipeline:

```bash
python main.py
```

The script will download the dataset from Kaggle if needed, preprocess the data, train both unsupervised and supervised models, and display evaluation plots.

## Notes

- The dataset source is the Kaggle dataset `devavratatripathy/ecg-dataset`.
- The downloaded file is saved to `data/ecg.csv` by default.
- Do not commit raw dataset files into the repository. The `data/` folder and `ecg.csv` are ignored by `.gitignore`.
- If the dataset column names differ from the assumed format, update `data_preprocessing.py` accordingly.
- The current configuration uses `tensorflow` for the autoencoder and `imbalanced-learn` for SMOTE.
