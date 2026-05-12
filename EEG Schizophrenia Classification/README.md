# 🧬 EEG Schizophrenia Classification

## 📌 Project Overview

This project develops a machine learning pipeline for **resting-state EEG-based classification of schizophrenia** using clinically validated EEG biomarkers. The system distinguishes patients with schizophrenia from healthy controls by analysing frontal alpha asymmetry, inter-hemisphere coherence, and complexity measures extracted from multichannel resting-state EEG recordings.

A **Leave-One-Subject-Out (LOSO)** cross-validation strategy is employed throughout to ensure subject-level generalization and avoid the data leakage common in EEG machine learning literature.

---

## 🎯 Objectives

- Extract and validate EEG biomarkers associated with schizophrenia (frontal asymmetry, coherence, complexity)
- Build a robust binary classification pipeline (schizophrenia vs. healthy controls)
- Apply LOSO cross-validation to produce clinically honest performance estimates
- Compare classical and sequence-based (LSTM) classification approaches

---

## 🧠 Methods & Techniques

- ICA-based removal of ocular and muscular artifacts
- Epoch extraction (2-second windows, 50% overlap)
- Feature extraction:
  - Band-power per channel (delta, theta, alpha, beta, gamma)
  - **Frontal alpha asymmetry index**
  - **Inter-hemisphere coherence**
  - Lempel-Ziv complexity
- Leave-One-Subject-Out (LOSO) cross-validation to prevent subject-level data leakage

### 📊 Evaluation Metrics

- LOSO Accuracy
- AUC-ROC
- Precision, Recall, F1-score
- Confusion Matrix

---

## 🤖 Models Implemented

- Logistic Regression (baseline)
- Support Vector Machine (SVM)
- Long Short-Term Memory (LSTM)

---

## 📊 Dataset

- **Schizophrenia EEG Dataset** — Resting-state EEG from schizophrenia patients and matched healthy controls
- Multichannel EEG recordings
- [Dataset Source (Kaggle)](https://www.kaggle.com/datasets/broach/button-tone-sz)

---

## 📈 Results

| Model | LOSO Accuracy | AUC |
|-------|--------------|-----|
| Logistic Regression | ~74% | ~0.80 |
| SVM | ~82% | ~0.88 |
| LSTM | ~85% | ~0.91 |

- LSTM captures temporal dynamics in EEG sequences, yielding the highest AUC
- SVM with connectivity features provides a strong, interpretable alternative
- LOSO validation ensures results reflect true cross-subject generalization

---

## 🔬 Research Significance

Schizophrenia diagnosis remains heavily reliant on clinical interview, introducing subjectivity and delay. This project explores **objective EEG biomarkers** — particularly frontal alpha asymmetry and inter-hemisphere coherence — as potential diagnostic markers, contributing to:

- Computational psychiatry and neuroimaging-based diagnostics
- Rigorous EEG ML methodology (LOSO validation, ICA artifact removal)
- Foundational work toward multimodal biomarker fusion for psychiatric classification

---

## 🛠️ Tech Stack

- **Programming:** Python
- **Signal Processing:** MNE-Python, SciPy
- **ML / DL:** scikit-learn, PyTorch
- **Data Handling:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Environment:** Jupyter Notebook, VS Code

---

## 📂 Project Structure

```
EEG-Schizophrenia-Classification/
│── preprocessing.py            # ICA-based artifact removal, epoch extraction
│── feature_extraction.py       # Coherence, band-power asymmetry, connectivity
│── classification.ipynb        # Multi-class classification pipeline
│── cross_validation.ipynb      # Leave-One-Subject-Out cross-validation
│── results/                    # Saved model outputs and evaluation metrics
└── README.md
```

---

## ⚙️ Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/khunsa123/Multimodal-NeuroPhysio-Signal-Research.git
cd EEG-Schizophrenia-Classification

# 2. Install dependencies
pip install numpy pandas scipy mne scikit-learn torch matplotlib seaborn

# 3. Download the dataset from Kaggle (see link above) and place in data/

# 4. Run preprocessing
python preprocessing.py

# 5. Run classification and cross-validation
jupyter notebook classification.ipynb
jupyter notebook cross_validation.ipynb
```

---

## 🚀 Future Work

- Multimodal fusion with fMRI or fNIRS data for richer psychiatric biomarkers
- Explainable AI (SHAP) to identify the most diagnostically significant EEG channels
- Extension to other psychiatric conditions (bipolar disorder, depression)
- Real-time classification pipeline for clinical screening tools

---

## 📬 Contact

**Khunsa Iftikhar**
📧 [khunsaiftikhar123@gmail.com](mailto:khunsaiftikhar123@gmail.com)
🔗 [linkedin.com/in/khunsa-iftikhar](https://www.linkedin.com/in/khunsa-iftikhar/)

---

⚠️ **Ethical Note:** The dataset used is publicly available and fully anonymised, shared under open-access terms for non-commercial research purposes. No patient-identifiable information is stored or processed.

