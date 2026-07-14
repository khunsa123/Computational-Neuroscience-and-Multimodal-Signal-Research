# 🧠 Multimodal Psychophysiology Pipeline — DS007537

### EEG • Eye Tracking • GSR • PPG • Machine Learning • Multimodal Fusion

**Google Colab Friendly • RAM Efficient • BIDS-Compliant • OpenNeuro**

> 📂 This project is part of the **[Multimodal-NeuroPhysio-Signal-Research](https://github.com/khunsa123/Multimodal-NeuroPhysio-Signal-Research)** repository.

---

# ⭐ Overview

The **Multimodal Psychophysiology Pipeline** is an end-to-end research workflow for processing and analyzing multimodal neurophysiological recordings from the **OpenNeuro DS007537** dataset.

The project integrates multiple physiological sensing modalities—including **EEG**, **eye tracking**, **Galvanic Skin Response (GSR)**, and **Photoplethysmography (PPG)**—to investigate cognitive load, visual attention, physiological arousal, and multimodal synchronization.

Rather than focusing on a single analysis, the repository is organized as a sequence of five complementary notebooks that progressively build from signal preprocessing and feature engineering to multimodal machine learning and precise cross-modal synchronization.

Designed for **Google Colab**, the pipeline streams data directly from OpenNeuro, minimizes memory usage through subject-wise processing, and follows the Brain Imaging Data Structure (BIDS) standard for reproducible neurophysiology research.

---

# 🎯 Project Objectives

This project demonstrates how multiple physiological sensing modalities can be combined to study human cognition and behavior.

The repository focuses on:

* EEG signal processing and spectral feature extraction
* Eye-tracking analysis (blinks, saccades, pupil dynamics)
* Physiological signal processing using GSR and PPG
* Multimodal feature engineering
* Cognitive load and arousal modeling
* Subject-independent machine learning
* Early and late multimodal fusion
* EEG–eye tracking synchronization and drift correction

---

# 📁 Dataset

**OpenNeuro DS007537**

The dataset contains multimodal recordings collected during smartphone interaction and video-viewing tasks.

Available modalities include:

* 66-channel EEG (1000 Hz)
* Head-mounted eye tracking
* Galvanic Skin Response (GSR)
* Photoplethysmography (PPG)
* Experimental event markers
* 23 participants
* Fully BIDS-compliant organization

Dataset:

https://openneuro.org/datasets/ds007537

---

# 🔬 Project Workflow

The repository is organized as a progressive multimodal analysis pipeline.

```text
OpenNeuro DS007537
        │
        ▼
────────────────────────────────────────
Data Acquisition & Streaming
────────────────────────────────────────
        │
        ▼
Signal Preprocessing
(EEG • Eye Tracking • GSR • PPG)
        │
        ▼
Feature Extraction
        │
        ▼
Notebook 01
Blink Detection + EEG Alpha
        │
        ▼
Notebook 02
Saccade Latency Analysis
        │
        ▼
Notebook 03
Multimodal Arousal Prediction
        │
        ▼
Notebook 04
Multimodal Fusion Model
        │
        ▼
Notebook 05
EEG–Eye Tracking Synchronization
        │
        ▼
Statistical Analysis & Machine Learning
```

---

# 📚 Project Structure

| Notebook                                     | Primary Focus                               | Main Techniques                                                                   |
| -------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------- |
| **01 — Blink Detection & Cognitive Load**    | Blink detection and EEG alpha analysis      | Blink detection, EEG spectral analysis, correlation analysis, Logistic Regression |
| **02 — Saccade Latency & Decision Making**   | Eye-movement timing and behavioral analysis | Velocity-based saccade detection, ANOVA, Tukey HSD, Linear Regression             |
| **03 — Pupil Dilation, Stress & Arousal**    | Multimodal physiological modeling           | GSR, PPG, pupil dynamics, Random Forest, Group K-Fold CV                          |
| **04 — Multimodal Fusion Model**             | Cognitive load classification               | Early vs. Late Fusion, Gradient Boosting, Feature Importance                      |
| **05 — Multimodal Synchronization Pipeline** | EEG and eye-tracking alignment              | Drift correction, stimulus-locked epoching, cross-modal analysis                  |

---

# 📂 Repository Structure

```text
Multimodal-Psychophysiology-DS007537/
│
├── notebooks/
│   ├── 01_blink_detection_cognitive_load.ipynb
│   ├── 02_saccade_latency_decision_making.ipynb
│   ├── 03_pupil_dilation_stress_arousal.ipynb
│   ├── 04_multimodal_fusion_model.ipynb
│   └── 05_multimodal_synchronization_pipeline.ipynb
│
├── src/                     # Reusable preprocessing and analysis modules
├── utils/                   # Helper functions and visualization utilities
├── config/                  # Configuration files
├── data/                    # Processed features and intermediate outputs
├── results/                 # Figures and result summaries
├── requirements.txt
└── README.md
```

---

# ⚙️ Key Methods

Across the five notebooks, the project implements:

### EEG Processing

* BrainVision EEG loading
* Band-pass filtering
* Alpha, theta, and beta spectral analysis
* Hilbert envelope extraction
* Trial-wise EEG feature computation

### Eye Tracking

* Blink detection
* Saccade detection
* Pupil preprocessing
* Pupil dynamics
* Gaze trajectory analysis

### Physiological Signals

* GSR preprocessing
* Skin conductance feature extraction
* Heart rate estimation
* Heart-rate variability (HRV)
* Signal normalization

### Statistical Analysis

* Pearson correlation
* Spearman correlation
* Independent t-tests
* One-way ANOVA
* Tukey HSD
* Linear regression
* Effect-size estimation

### Machine Learning

* Logistic Regression
* Random Forest
* Gradient Boosting
* Group K-Fold Cross-Validation
* Hyperparameter optimization
* Early and Late Multimodal Fusion

---

# 📊 Project Outputs

The pipeline produces:

* Trial-wise multimodal feature datasets
* Blink and saccade event tables
* EEG spectral features
* Physiological feature matrices
* Synchronized multimodal epochs
* Machine learning models
* Statistical summaries
* Publication-quality visualizations

Representative figures include:

* Correlation plots
* ROC curves
* Confusion matrices
* Feature importance rankings
* Latency distributions
* Gaze trajectory visualizations
* Synchronization diagnostics

---

# 💻 Installation

Clone the repository and install the required dependencies.

```bash
git clone https://github.com/khunsa123/Multimodal-NeuroPhysio-Signal-Research.git

cd Multimodal-NeuroPhysio-Signal-Research/Multimodal-Psychophysiology-DS007537

pip install -r requirements.txt
```

---

# ☁️ Running in Google Colab

All notebooks are designed for efficient execution in Google Colab.

Key characteristics include:

* Direct streaming from OpenNeuro where applicable
* Subject-wise processing to reduce memory usage
* Modular preprocessing functions
* Automatic memory cleanup
* Optional downsampling for large recordings

The notebooks are intended to run without downloading the complete dataset locally.

---

# 🧪 Research Applications

The pipeline is applicable to research in:

* NeuroAI
* Human–Computer Interaction (HCI)
* Brain–Computer Interfaces (BCI)
* Cognitive Neuroscience
* Psychophysiology
* Biomedical Signal Processing
* Multimodal Machine Learning

---

# ⚠️ Notes on Interpretation

Several notebooks use physiology-derived surrogate labels (for example, EEG alpha power or physiological arousal indices) to support exploratory modeling in the absence of externally annotated cognitive-state labels.

Accordingly, classification performance should be interpreted as prediction of physiology-derived indices rather than independently validated psychological or clinical outcomes.

---

# ⚖️ Ethical Considerations

This project uses the publicly available, de-identified **OpenNeuro DS007537** dataset in accordance with its published data-sharing and usage policies.

No personally identifiable information is processed, stored, or redistributed.

---

# 📬 Contact

**Khunsa Iftikhar**

**Data Scientist • NeuroAI Researcher**

📧 **Email:** [khunsaiftikhar123@gmail.com](mailto:khunsaiftikhar123@gmail.com)

💻 **GitHub:** https://github.com/khunsa123

🎓 **Google Scholar:** https://scholar.google.com/citations?hl=en&user=Q-mM508AAAAJ
