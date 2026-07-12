# 📄 04 — Multimodal Fusion Model for Cognitive Load Classification (DS007537)

### EEG + Eye Tracking + GSR + PPG • Early vs. Late Fusion • Gradient Boosting
📂 **Part of:** *Multimodal Psychophysiology Pipeline — DS007537*
📓 **Notebook:** `04_multimodal_fusion_model.ipynb`

---

# ⭐ Overview
This notebook develops a multimodal machine learning pipeline for cognitive load classification using synchronized neurophysiological and physiological signals from the **OpenNeuro DS007537** dataset.

The analysis integrates four complementary sensing modalities:

- **EEG** (spectral brain activity)
- **Eye Tracking** (blink rate)
- **Galvanic Skin Response (GSR)**
- **Photoplethysmography (PPG)**
A key objective is to compare **early fusion** and **late fusion** strategies for combining multimodal features and to evaluate whether integrating multiple physiological signals improves cognitive load prediction.

The notebook is designed for **Google Colab**, processes subjects individually to minimize memory usage, and follows a modular, BIDS-compatible workflow.

---

# 🧠 Research Questions
This notebook investigates the following questions:

1. Does multimodal fusion improve cognitive load classification compared with individual modalities?
2. Which physiological modalities contribute most to prediction performance?
3. Does early feature fusion outperform late decision fusion?
4. How informative are EEG spectral features relative to autonomic physiological measures?

---

# 📁 Dataset
**OpenNeuro DS007537**

The notebook uses data collected from **23 participants** performing smartphone interaction and video-viewing tasks.

Available modalities include:

- 66-channel EEG (BrainVision format)
- Head-mounted eye tracking
- Galvanic Skin Response (GSR)
- Photoplethysmography (PPG)
- Event markers
- Fully BIDS-compliant organization

---

# 🔧 Pipeline Overview
The multimodal workflow consists of five major stages.

## 1. EEG Feature Extraction
EEG recordings are processed using **MNE-Python**.

Processing includes:

- Loading BrainVision recordings
- EEG channel selection
- Spectral filtering
- Power spectral analysis
For every trial, spectral power is extracted from:

- Theta band
- Alpha band
- Beta band
These features capture neural activity associated with attention, cognitive effort, and information processing.

---

## 2. Physiological Feature Extraction
Physiological features from previous notebooks are incorporated into the fusion model.

### Eye Tracking

- Blink rate per trial

### GSR

- Mean tonic skin conductance
- Phasic peak count

### PPG

- Heart rate (HR)
- Heart-rate variability (RMSSD)

---

## 3. Multimodal Feature Construction
Each trial is represented by a unified feature vector.

ModalityExtracted FeaturesEEGTheta power, Alpha power, Beta powerEye TrackingBlink rateGSRTonic level, Phasic peak countPPGHeart rate, HRV (RMSSD)
---

## 4. Fusion Strategies
Two multimodal fusion approaches are evaluated.

### Early Fusion
All extracted features are concatenated into a single feature vector before model training.

```
EEG Features
        │
Eye Tracking
        │
GSR Features
        │
PPG Features
        ▼
Feature Concatenation
        ▼
Gradient Boosting Classifier
```
**Advantages**

- Learns interactions across modalities
- Maximizes available information
- Highest predictive performance

---

### Late Fusion
Independent classifiers are trained for each modality.

Predicted probabilities are combined to generate the final prediction.

```
EEG Model ─┐
Eye Model ─┤
GSR Model ─┤──► Probability Fusion
PPG Model ─┘
                │
                ▼
        Final Prediction
```
**Advantages**

- Robust to missing modalities
- Easier interpretation of modality-specific performance
- More flexible deployment

---

## 5. Cognitive Load Labeling
A surrogate cognitive-load index is constructed using trial-wise EEG alpha power.

- **High cognitive load:** Alpha power below the subject median
- **Low cognitive load:** Alpha power above the subject median
**Note:** Because cognitive-load labels are derived from EEG alpha power, and EEG spectral features are also included in the feature set, the reported classification results should be interpreted as prediction of an EEG-derived cognitive-load index rather than an independently annotated cognitive state.

---

# 🤖 Machine Learning

## Classification Model

- Gradient Boosting Classifier
- Subject-independent evaluation using Group K-Fold cross-validation
- Feature standardization
- Class imbalance handling through weighting and threshold tuning

---

# 📊 Results

## Early Fusion
MetricPerformanceAccuracy~0.82ROC-AUC~0.86Key observations:

- Best overall performance
- Strongest multimodal interactions
- EEG features dominate prediction
- Physiological features improve robustness

---

## Late Fusion
MetricPerformanceAccuracy~0.75ROC-AUC~0.79Key observations:

- Lower predictive accuracy
- Better tolerance to missing or noisy modalities
- Improved interpretability through modality-specific models

---

# 📈 Feature Importance
The Gradient Boosting model identifies the following variables as the most informative:

RankFeature1EEG Alpha Power2EEG Theta Power3GSR Phasic Peaks4Heart Rate5Blink Rate6EEG Beta PowerThe results indicate that neural activity provides the strongest predictive signal, while autonomic physiological measures contribute complementary information.

---

# 📊 Generated Outputs
The notebook produces:

- Trial-wise multimodal feature matrix
- Early fusion classification results
- Late fusion classification results
- Feature importance rankings
- ROC curve
- Confusion matrix
- Performance comparison between fusion strategies

---

# 🧩 Key Findings

- Early fusion achieves higher classification performance than late fusion.
- EEG spectral features provide the strongest indicators of cognitive load.
- GSR, PPG, and eye-tracking features improve model robustness by contributing complementary physiological information.
- Multimodal integration consistently outperforms single-modality analysis for this dataset.
- Subject-independent validation supports the generalizability of the multimodal pipeline across participants.

---

# 🚀 Position Within the Project
This notebook integrates the outputs of the previous analyses into a unified multimodal learning framework.

Previous notebooks contributed:

- **Notebook 01:** Blink rate extraction
- **Notebook 02:** Eye-movement characterization
- **Notebook 03:** GSR and PPG feature engineering
The final notebook extends this work by performing precise temporal synchronization between EEG and eye-tracking signals for stimulus-locked multimodal analyses.

---

# 🏁 Summary
This notebook presents a complete multimodal cognitive-load classification pipeline using EEG, eye tracking, GSR, and PPG data from the OpenNeuro DS007537 dataset. It compares early and late fusion strategies, extracts interpretable physiological features, and evaluates subject-independent machine learning models. The results demonstrate that combining complementary neurophysiological and physiological signals improves cognitive-load prediction, with early feature fusion providing the strongest overall performance for this dataset.
