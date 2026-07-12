# 🧠 Multimodal Psychophysiology Pipeline — DS007537
### EEG + Eye Tracking + GSR + PPG (OpenNeuro)

**Colab-Friendly • RAM-Efficient • BIDS-Compliant • Research-Ready**

> 📂 This is a project sub-folder within the [Multimodal-NeuroPhysio-Signal-Research](https://github.com/khunsa123/Multimodal-NeuroPhysio-Signal-Research) repository.

---

## ⭐ Overview

This project implements a complete multimodal psychophysiology pipeline built on the [OpenNeuro DS007537](https://openneuro.org/datasets/ds007537) dataset, which includes:

- 66-channel EEG (1000 Hz)
- Head-mounted eye tracking
- Galvanic Skin Response (GSR)
- Photoplethysmography (PPG)
- Smartphone interaction + video viewing tasks
- 23 subjects
- Fully BIDS-formatted

The pipeline is designed for:

- Cognitive load modelling
- Blink / saccade / pupil analysis
- Multimodal fusion
- EEG–eye tracking synchronization
- Machine learning on psychophysiology signals
- Google Colab execution with minimal RAM usage

---

## 🎯 Project Goals

This project implements **five independent research notebooks**, each self-contained and Colab-ready:

1. **Blink Detection + Cognitive Load**
2. **Saccade Latency + Decision Making**
3. **Pupil Dilation + Stress/Arousal**
4. **Multimodal Fusion Model**
5. **EEG + Eye Tracking Synchronization Pipeline**

Each notebook is lightweight, modular, and optimized for **streaming data** rather than downloading the full dataset. The repository also includes companion documentation for the later notebooks and organized outputs under the data and results folders.

---

## 📁 Folder Structure

```
Multimodal-Psychophysiology-DS007537/
│
├── notebooks/               # Jupyter notebooks for the five analyses
├── src/                     # Reusable Python modules
├── data/                    # Processed features, trial outputs, and intermediate datasets
├── results/                 # Figures, plots, and result summaries
├── config/                  # Dataset and preprocessing configuration files
├── utils/                   # Helper utilities and plotting functions
├── requirements.txt         # Python dependencies
└── README.md                # Project overview
```

---

## 📘 Notebooks

### 01 — Blink Detection + Cognitive Load
- Detect blinks from eye-tracking data
- Compute blink rate per trial
- Extract EEG alpha power
- Correlate blink rate ↔ cognitive load
- Train a lightweight classifier

### 02 — Saccade Latency + Decision Making
- Detect saccades using velocity thresholding
- Compute saccade latency + amplitude
- Link saccade latency to smartphone interaction behavior

### 03 — Pupil Dilation + Stress/Arousal
- Baseline-correct pupil dilation
- Extract GSR peaks + PPG HR/HRV
- Build arousal labels
- Train ML model to predict arousal

### 04 — Multimodal Fusion Model
- Merge EEG + eye tracking + GSR + PPG features
- Compare early vs. late fusion strategies
- Train a gradient boosting classifier for cognitive load
- Analyze feature importance across modalities

### 05 — EEG + Eye Tracking Synchronization Pipeline
- Align EEG and eye-tracking timestamps
- Apply drift correction
- Extract synchronized multimodal trial windows
- Perform cross-modal analyses and effect-size estimation

---

## 🔧 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

**Core libraries used:**
- MNE
- pandas
- numpy
- scipy
- scikit-learn
- matplotlib / seaborn
- pyEDFlib
- neurokit2

---

## ☁️ Running in Google Colab

All notebooks are designed for:

- Streaming directly from OpenNeuro when needed
- Low RAM usage
- Subject-wise processing
- Saving extracted features instead of raw signals

Each notebook includes:

- Memory-safe data loading
- Automatic cleanup routines
- Downsampling options
- Modular feature extraction functions

---

## 🧪 Research Relevance

This project demonstrates:

- Multimodal signal processing
- Cognitive load modelling
- Psychophysiology feature engineering
- Synchronization of heterogeneous sensors
- ML classification on multimodal data
- BIDS-compliant pipeline design
- Real-world human–computer interaction (HCI) analysis

Relevant for NeuroAI, BCI, and HCI research contexts, including multimodal psychophysiology and cognitive-state modelling tracks.

---

## ⚖️ Ethical & Data Note

This project uses the publicly available, de-identified **OpenNeuro DS007537** dataset under its stated data use terms. No personally identifiable information is processed or stored as part of this pipeline.

---

## 📬 Contact

**Khunsa Iftikhar**

Data Scientist • NeuroAI Researcher

- 📧 khunsaiftikhar123@gmail.com
- 💻 [GitHub](https://github.com/khunsa123)
- 🎓 [Google Scholar](https://scholar.google.com/citations?hl=en&user=Q-mM508AAAAJ)
