# 📄 README — Project 4: Multimodal Fusion Model for Cognitive Load Classification (DS007537)

### EEG + GSR + PPG + Eye-Tracking + Gradient Boosting + Early/Late Fusion

## ⭐ Overview
This notebook implements a multimodal cognitive load classification pipeline using physiological and neurophysiological signals from the OpenNeuro dataset DS007537. It integrates EEG, GSR, PPG, and eye-tracking blink rate into a unified machine learning model capable of distinguishing High vs. Low cognitive load.

This is the most comprehensive project in the multimodal suite, demonstrating full-stack neurophysiology fusion and subject-independent machine learning.

## 🧠 Research Questions
1. Does multimodal fusion improve cognitive load classification?
2. Which modalities contribute most to cognitive load prediction?
3. Does early fusion outperform late fusion?
4. Can EEG spectral features significantly boost performance?

## 📁 Dataset
OpenNeuro DS007537

- EEG (BrainVision format)
- Eye tracking (blink rate)
- GSR (skin conductance)
- PPG (pulse waveform → HR + HRV)
- 23 subjects
- Fully BIDS-formatted

## 🔧 Pipeline Summary

### 1. EEG Preprocessing (MNE + NeuroKit2)
For each subject:

- Load BrainVision EEG files (.vhdr, .vmrk, .eeg)
- Apply band-specific filtering for theta, alpha, and beta bands
- Extract power spectral density using MNE and NeuroKit2 tools
- Compute trial-wise EEG features such as mean theta, alpha, and beta power

These features capture cognitive load signatures such as reduced alpha power and increased theta activity under higher load.

### 2. Physiological Features (GSR + PPG + Eye Tracking)
From previous projects:

- GSR: tonic level and phasic peak count
- PPG: heart rate and HRV (RMSSD)
- Eye tracking: blink rate per trial

### 3. Fusion Strategies
Two fusion approaches were implemented:

#### Early Fusion
All features were concatenated into one vector:

```python
[alpha, beta, theta, gsr_tonic, gsr_peaks, hr, hrv, blink_rate]
```

Model: Gradient Boosting Classifier

Advantages:
- Captures cross-modal interactions
- Strong performance
- Single unified model

#### Late Fusion
Separate models were trained per modality:

- EEG model
- GSR model
- PPG model
- Eye-tracking model

Final prediction was obtained by averaging the probabilities.

Advantages:
- Robust to missing modalities
- Interpretable per-modality contributions

### 4. Cognitive Load Labeling
Cognitive load was defined using EEG alpha power:

- High load: alpha power below median
- Low load: alpha power above median

## 📊 Results and Performance

### Early Fusion
- Accuracy: approximately 0.82
- ROC-AUC: approximately 0.86
- Best performance across all tested models
- EEG features contributed the strongest signal
- Physiological features improved robustness

### Late Fusion
- Accuracy: approximately 0.75
- ROC-AUC: approximately 0.79
- More stable across subjects
- Lower performance than early fusion
- Useful when modalities are missing or noisy

### Feature Importance
Top predictors included:
1. EEG alpha power
2. EEG theta power
3. GSR phasic peaks
4. Heart rate (PPG)
5. Blink rate
6. Beta power

## 🔍 Modeling Details
- Group K-fold cross-validation for subject-independent evaluation
- Class imbalance handling through weighting and threshold tuning
- Gradient Boosting used for nonlinear interactions and feature importance analysis

## 🧠 Interpretation and Insights
- EEG is the strongest predictor of cognitive load
- GSR, PPG, and blink rate add robustness and contextual information
- Early fusion outperforms late fusion
- Multimodal integration is essential for improved classification

## 🚀 Future Work
This notebook forms the fourth major component of the multimodal psychophysiology research suite. It sets the stage for Project 5, which focuses on EEG and eye-tracking synchronization.

## 🏁 Summary
This notebook establishes a complete multimodal cognitive load classification pipeline involving EEG spectral feature extraction, physiological signal integration, early versus late fusion, gradient boosting classification, subject-independent evaluation, and feature importance analysis.
