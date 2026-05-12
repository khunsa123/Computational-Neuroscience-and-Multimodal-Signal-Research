# 🔥 Pain‑Evoked EEG Analysis (Laser‑Evoked Potentials — ds002338)

This project analyzes **laser‑evoked pain EEG responses** using the open‑access dataset **ds002338** from OpenNeuro.  
It extracts **pain‑evoked potentials (LEPs)**, performs **ERP and time–frequency analysis**, and builds **machine learning models** to classify **pain vs non‑pain** trials.

This project is directly aligned with research themes at the **Center for Neuroplasticity and Pain (CNAP)**, including:
- cortical pain processing  
- laser‑evoked potentials (N2/P2)  
- pain biomarkers  
- neuroplasticity in nociceptive pathways  

---

## 📌 Dataset Overview

**Dataset:** OpenNeuro *ds002338*  
**Modality:** EEG  
**Task:** Laser‑evoked pain stimulation  
**Subjects:** Multiple healthy participants  
**Format:** BIDS‑compliant  
**Size:** ~150–200 MB (ideal for Google Colab)

Each trial contains:
- **Painful laser stimuli**
- **Non‑painful control stimuli**
- EEG recorded at high temporal resolution

---

## 📂 Project Structure

Pain_EEG_Analysis/
│
├── notebooks/
│   ├── 01_download_and_preprocess.ipynb
│   ├── 02_erp_analysis.ipynb
│   ├── 03_ml_classification.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   ├── ml_models.py
│   ├── visualization.py
│
├── data/                # downloaded automatically (ignored by git)
├── README.md
└── requirements.txt

---

## 🧪 Methods

### **1. Preprocessing**
- Load BIDS dataset with MNE‑Python  
- Bandpass filter (1–40 Hz)  
- Notch filter (50 Hz)  
- ICA artifact removal (ocular/muscle)  
- Epoching around laser stimuli (−0.2 to 0.8 s)

### **2. ERP Analysis**
- Extract N2/P2 components  
- Compare pain vs non‑pain ERPs  
- Plot:
  - grand averages  
  - topomaps  
  - butterfly plots  

### **3. Time–Frequency Analysis**
- Morlet wavelets  
- Alpha suppression  
- Gamma bursts  
- Pain‑specific oscillatory signatures  

### **4. Machine Learning Classification**
- Feature extraction:
  - N2 amplitude  
  - P2 amplitude  
  - Peak latencies  
  - Band‑power features  
- Models:
  - Logistic Regression  
  - SVM  
  - Random Forest  
- Evaluation:
  - Accuracy  
  - ROC‑AUC  
  - Confusion matrix  

---

## ▶️ Quick Start (Google Colab)

Run the full pipeline:

```python
!pip install mne openneuro-py

from openneuro import download
download(dataset="ds002338", target_dir="/content/ds002338", include=["sub-01"])
Then open the notebook:
notebooks/01_download_and_preprocess.ipynb

📊 Expected Results
Clear N2/P2 components for pain trials

Strong ERP differences between pain vs non‑pain

ML classifier accuracy typically 70–85% depending on features

Time–frequency signatures consistent with nociceptive processing

📝 Notes
Only one subject is needed for demonstration; more subjects improve robustness.

All preprocessing steps follow standard EEG pain‑evoked potential pipelines.

Dataset is small and ideal for Colab.

👩‍🔬 Author
Khunsa Iftikhar  
Computational Neuroscience & AI Researcher
Multimodal Neurophysiology & Machine Learning
