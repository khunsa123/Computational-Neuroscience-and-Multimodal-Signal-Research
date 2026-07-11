# 🧠 Multimodal NeuroPhysio Signal Research

## 📌 Repository Overview

This repository documents a portfolio of computational neuroscience and psychophysiology research projects focused on multimodal neurophysiological and physiological signal analysis. It brings together EEG, iEEG, ECoG, EMG, ECG, eye tracking, and peripheral physiological signals (GSR, PPG) — alongside neuroimaging-inspired modeling — to advance biomarker discovery, subject-generalizable decoding, and translational neurotechnology.

> Projects are organized in dedicated folders with project-level `README.md`, code, analysis notebooks, and dataset references.

---

## 🎯 Research Theme

> My research focuses on multimodal computational neuroscience and psychophysiology for decoding pain, cognition, motor function, and cognitive/affective states using EEG, ECoG, EMG, eye tracking, peripheral physiology, and fMRI, with emphasis on biomarker discovery, cross-subject generalization, and neurophysiological modeling.


**Scientific question:**

> How can multimodal neurophysiological and physiological signals be integrated to decode cognitive, affective, and motor states in clinically and behaviorally meaningful ways?

---

## 🧠 Computational Neuroscience & Psychophysiology Domains

| Domain | Main Data Types |
|---|---|
| Cognitive neuroscience | EEG, MEG, fMRI |
| Clinical neurophysiology | EEG, iEEG, ECoG, EMG |
| BCI / neuroengineering | EEG, EMG, fNIRS |
| Computational psychiatry | EEG, fMRI |
| Neuroimaging AI | MRI, fMRI, EEG |
| Pain neuroscience | EEG, iEEG, ECoG, fMRI, autonomic signals |
| Rehabilitation neuroscience | EMG, EEG, motion |
| Psychophysiology / HCI | EEG, eye tracking, GSR, PPG |

---

## 🎯 Research Goals

- Develop interpretable ML/DL pipelines for neurophysiological and psychophysiological biomarkers
- Evaluate cross-subject generalization using subject-wise and LOSO validation
- Compare classical and deep learning methods for EEG/ECoG/EMG decoding
- Translate pain, cognition, and motor function decoding into publication-quality research
- Expand toward multimodal fusion with neuroimaging, BCI, and psychophysiology paradigms (eye tracking, GSR, PPG)

---

## 📁 Projects

| # | Project | Signal Type | Key Focus | Status |
|---|---------|------------|-----------|--------|
| 1 | [EEG Epilepsy Data Analysis](./EEG%20Epilepsy%20Data%20Analysis/) | EEG | Seizure detection, waveform features, CNN/ML fusion | ✅ Complete |
| 2 | [EEG Schizophrenia Classification](./EEG%20Schizophrenia%20Classification/) | EEG | Resting-state diagnosis, LOSO, LSTM + classical ML | ✅ Complete |
| 3 | [ECG-Anomaly-Detection-&_Classification](./ECG-Anomaly-Detection-&_Classification/) | ECG | Anomaly detection, autoencoder, ensemble classifiers | ✅ Complete |
| 4 | [EEG-BCI-Research-Copilot](./EEG-BCI-Research-Copilot/) | EEG | BCI feature engineering, neural decoding, human-in-the-loop workflow | ✅ Complete |
| 5 | [Laser‑Evoked Pain EEG Analysis](./Laser%E2%80%91Evoked%20Pain%20EEG%20Analysis/) | EEG | Pain biomarker discovery, laser-evoked potentials, manuscript preparation | ✅ Complete / manuscript in progress |
| 6 | [EMG-Stroke-Recovery-Monitoring](./EMG-Stroke-Recovery-Monitoring/) | EMG | Motor recovery monitoring, feature extraction, rehabilitation analytics | 🔄 In progress |
| 7 | [Multimodal Motor Imagery Analysis](./Multimodal%20Motor%20Imagery%20Analysis/) | EEG / EMG | Motor imagery decoding, sensor fusion, BCI benchmarking | 🔄 In progress |
| 8 | [Somatosensory Pain iEEG-ECoG Analysis](./Somatosensory%20Pain%20iEEG-ECoG%20Analysis/) | iEEG / ECoG | Pain decoding, neurophysiological modeling, translational analysis | 🔄 In progress |
| 9 | [Multimodal Psychophysiology Pipeline — DS007537](./Multimodal-Psychophysiology-DS007537/) | EEG / Eye Tracking / GSR / PPG | Cognitive load modeling, blink/saccade/pupil analysis, multimodal fusion, EEG–eye tracking synchronization | 🔄 In progress |

---

## 🧠 Research Domains

- ⚡ **EEG / ECoG Pain Decoding** — Laser-evoked potentials, somatosensory processing, biomarker extraction
- 🧠 **Cognitive and Psychiatric EEG** — Schizophrenia classification, attention and cognition modeling
- 💪 **Motor Function & BCI** — Motor imagery analysis, EMG-based stroke recovery monitoring, EEG-BCI research
- ❤️ **Clinical Signal Analytics** — ECG/EMG anomaly detection, clinical biomarker validation
- 👁️ **Multimodal Psychophysiology & HCI** — Eye tracking, GSR, and PPG fusion with EEG for cognitive load, arousal, and human-computer interaction modeling
- 🔗 **Multimodal Generalization** — Cross-subject validation, fusion of EEG/EMG/ECoG/peripheral physiology, and future fMRI-informed models

---

## 🛠️ General Tech Stack

| Category | Tools & Libraries |
|----------|------------------|
| **Languages** | Python |
| **Signal Processing** | MNE-Python, SciPy, NumPy, neurokit2, pyEDFlib |
| **ML / DL Frameworks** | scikit-learn, TensorFlow, PyTorch |
| **Data Processing** | Pandas, imbalanced-learn (SMOTE) |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Environments** | Jupyter Notebook, VS Code, Google Colab |

---

## 📂 Repository Structure

```
Multimodal-NeuroPhysio-Signal-Research/
│
├── EEG Epilepsy Data Analysis/            # EEG seizure and epilepsy signal analysis
├── EEG Schizophrenia Classification/      # Resting-state EEG psychiatric classification
├── ECG-Anomaly-Detection-&_Classification/ # ECG anomaly detection and classification
├── EEG-BCI-Research-Copilot/              # EEG-based BCI research workflows
├── Laser‑Evoked Pain EEG Analysis/         # Pain biomarker analysis from laser-evoked EEG
├── EMG-Stroke-Recovery-Monitoring/        # EMG monitoring for motor recovery research
├── Multimodal Motor Imagery Analysis/     # Motor imagery decoding and multimodal fusion
├── Somatosensory Pain iEEG-ECoG Analysis/ # iEEG/ECoG pain decoding and modeling
├── Multimodal-Psychophysiology-DS007537/  # EEG + eye tracking + GSR + PPG multimodal pipeline
└── README.md                              # ← You are here
```

---

## 🔬 Research Standards

All projects in this repository follow rigorous research practices:

- **Reproducibility** — Fixed random seeds, transparent preprocessing, and notebook-driven workflows
- **Cross-study validation** — LOSO and subject-wise evaluation for generalization
- **Ethical datasets** — Publicly available, anonymised research datasets used for non-commercial research
- **No data leakage** — Subject-level splits enforced across training and testing
- **Publication readiness** — Manuscript and results documentation aligned with journal-ready standards

---

## 📌 Current Focus

- Finalising code and manuscript details for **Laser‑Evoked Pain EEG Analysis**
- Advancing multimodal decoding in **Motor Imagery** and **Somatosensory Pain iEEG/ECoG**
- Building out the multimodal **Psychophysiology Pipeline (DS007537)** for cognitive load and EEG–eye tracking synchronization
- Strengthening cross-subject generalization and biomarker interpretability across projects

---

## 🔗 Related Publications

- **Ahmed, W., Riaz, S., Iftikhar, K., Konur, S.** (2023). *Speech Emotion Recognition Using Deep Learning.* Springer LNCS Vol. 14381, SGAI 2023.
- **In preparation:** Iftikhar, K., Nisar, M.W. *EEG-Based Attention and Cognitive State Analysis Using Consumer-Grade BCI Devices.*

---

## 👩‍🔬 Author

**Khunsa Iftikhar**

MSc Big Data Science (Distinction), University of Bradford, UK

🔗 [Google Scholar](https://scholar.google.com/citations?hl=en&user=Q-mM508AAAAJ) | [LinkedIn](https://www.linkedin.com/in/khunsa-iftikhar/) | [Website](https://sites.google.com/view/khunsa-iftikhar/)

📧 khunsaiftikhar123@gmail.com

---

⚠️ **Ethical Note:** All datasets used across this repository are publicly available, anonymised, and appropriate for research use.
