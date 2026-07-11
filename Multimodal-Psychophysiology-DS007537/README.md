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

Each notebook is lightweight, modular, and optimized for **streaming data** rather than downloading the full dataset.

---

## 📁 Folder Structure

```
Multimodal-Psychophysiology-DS007537/
│
├── notebooks/               # Colab notebooks for each project
├── src/                     # Python modules for data loading, preprocessing, features
├── data/                    # Extracted features + synchronized trials
├── config/                  # Dataset + parameter configs
├── utils/                   # Plotting + helper utilities
└── README.md                # This file
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
- Gradient boosting classifier for cognitive load

### 05 — EEG + Eye Tracking Synchronization Pipeline
- Align EEG and eye-tracking timestamps
- Drift correction
- Extract synchronized multimodal trial windows
- Export unified trial-wise dataset

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
- eegdash *(optional)*

---

## ☁️ Running in Google Colab

All notebooks are designed for:

- Streaming directly from OpenNeuro (no full dataset download required)
- Low RAM usage (<3GB)
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
