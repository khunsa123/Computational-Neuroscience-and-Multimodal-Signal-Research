# 🔥 Laser‑Evoked Pain EEG Analysis (OpenNeuro ds002338)

This project develops and validates a **robust EEG‑based pipeline for objective pain detection**, using the OpenNeuro **ds002338** laser‑evoked pain dataset (N = 24). The analysis integrates advanced EEG preprocessing, multidomain feature engineering, machine learning, and source localization to identify reliable neural biomarkers of nociceptive processing.

This work is directly aligned with research themes in **pain neurophysiology**, **nociceptive evoked potentials**, and **objective pain assessment**, and is currently being prepared as a manuscript for publication.

---

## 📌 Objectives

- Identify electrophysiological biomarkers of laser‑evoked pain  
- Build a generalizable ML pipeline for pain vs non‑pain classification  
- Validate neural signatures using source localization  
- Evaluate cross‑subject generalization using LOSO CV  

---

## 🧪 Methods

### **1. Preprocessing**
- ICA‑based artifact rejection  
- Bandpass filtering (1–40 Hz)  
- Epoching around laser stimuli (−0.2 to 0.8 s)  
- Baseline correction  
- Artifact removal and trial‑level quality control  

### **2. Feature Engineering**
**ERP Features**
- N2 amplitude  
- P2 amplitude  
- Peak latencies  
- Global field power  

**Spectral Features**
- Theta power  
- Theta/Beta Ratio (TBR)  
- Broadband spectral power  

**Hjorth Parameters**
- Activity  
- Mobility  
- Complexity  

### **3. Machine Learning**
- SMOTE oversampling to address 8:1 class imbalance  
- Random Forest, SVM, Logistic Regression  
- **Leave‑One‑Subject‑Out (LOSO)** cross‑validation  
- Feature importance analysis  

### **4. Source Localization**
- LCMV beamforming  
- Noise covariance estimation  
- Anatomical mapping to cortical pain regions  

---

## 📊 Key Results

### **1. Dominant Biomarker: N2 Amplitude**
- N2 amplitude showed the strongest group‑level effect  
- **Cohen’s d = −1.337, p < 0.001**  
- Indicates early nociceptive processing is the primary discriminator  

### **2. Source Localization**
- LCMV beamformer localized differential activity to the **caudal Anterior Cingulate Cortex (ACC)**  
- **Effect size: d = 0.832**  
- Provides anatomical validation consistent with known pain‑processing hubs  

### **3. Classification Performance**
Using ERP + Spectral + Hjorth features:

| Metric | Score |
|--------|--------|
| Cross‑Validation Accuracy | **90.14%** |
| LOSO Accuracy | **86.03%** |
| F1‑Score (Pain Class) | High stability across subjects |

These results demonstrate **generalizable neural signatures of pain**, not limited to individual subjects.

### **4. Spectral Insights**
- Theta/Beta Ratio (TBR) shifts during pain  
- Distributed cortical engagement beyond focal ERP peaks  
- Complementary to ERP‑based biomarkers  

---

## 📂 Repository Structure

Laser_Evoked_Pain_EEG_Analysis/

│
├── notebooks/

│   ├── 01_preprocessing.ipynb

│   ├── 02_feature_engineering.ipynb

│   ├── 03_ml_classification.ipynb

│   ├── 04_source_localization.ipynb

│
├── src/

│   ├── preprocessing.py

│   ├── features.py

│   ├── ml_models.py

│   ├── source_localization.py

│   ├── visualization.py

│
├── results/

│   ├── erp_plots/

│   ├── source_maps/

│   ├── ml_metrics/

│
├── README.md

└── requirements.txt

---

## ▶️ Quick Start (Google Colab)

```python
!pip install mne openneuro-py numpy scipy scikit-learn matplotlib
```

```bash
from openneuro import download
download("ds002338", target_dir="/content/ds002338", include=["sub-01"])
```
---

📝 Manuscript Status
This work is currently being prepared as:

Iftikhar, K. (in prep). Laser‑Evoked Pain EEG Biomarkers: ERP, Spectral, and Source‑Level Signatures for Objective Pain Detection.

---
👩‍🔬 Author
Khunsa Iftikhar  
Computational Neuroscience & AI Researcher
EEG • Pain Neurophysiology • Machine Learning
GitHub: https://github.com/khunsa123
