# 📄 03 — Pupil Dilation, Stress & Arousal Prediction (DS007537)

### Pupil Dynamics + GSR + PPG • Multimodal Physiological Analysis • Random Forest Classification

📂 **Part of:** *Multimodal Psychophysiology Pipeline — DS007537*
📓 **Notebook:** `03_pupil_dilation_stress_arousal.ipynb`

---

# ⭐ Overview

This notebook develops a multimodal physiological pipeline for **arousal prediction** using synchronized pupil dynamics, Galvanic Skin Response (GSR), and Photoplethysmography (PPG) signals from the **OpenNeuro DS007537** dataset.

The workflow combines signal preprocessing, feature engineering, multimodal integration, and subject-independent machine learning to investigate how autonomic and ocular physiological responses relate to changes in psychophysiological arousal.

Designed for **Google Colab**, the notebook streams data directly from OpenNeuro, processes subjects individually to minimize memory usage, and follows a modular, BIDS-compatible workflow.

---

# 🧠 Research Questions

This notebook investigates the following questions:

1. Can multimodal physiological signals predict arousal states?
2. Which physiological modalities contribute most to prediction performance?
3. Does subject-independent machine learning generalize across participants?
4. Do pupil dynamic features improve multimodal arousal prediction?

---

# 📁 Dataset

**OpenNeuro DS007537**

The notebook analyzes recordings from **23 participants**, including:

* Pupil diameter (left and right eyes)
* Galvanic Skin Response (GSR)
* Photoplethysmography (PPG)
* Smartphone interaction task
* Fully BIDS-compliant organization

---

# 🔧 Pipeline Overview

The analysis consists of five major stages.

---

## 1. Multimodal Data Acquisition

Physiological recordings are streamed directly from the OpenNeuro dataset without requiring a complete local download.

Signals extracted include:

* Pupil diameter
* GSR
* PPG

All modalities are resampled to a common **10 Hz timeline**, producing synchronized physiological recordings suitable for multimodal analysis.

---

## 2. Signal Preprocessing

Each modality undergoes preprocessing to improve signal quality and consistency.

### Pupil Processing

* Blink interpolation
* Missing-value correction
* Baseline correction
* Rolling-average smoothing

### GSR Processing

* Butterworth low-pass filtering
* Z-score normalization

### PPG Processing

* Low-pass filtering
* Heart-rate normalization

These preprocessing steps reduce noise while preserving physiologically meaningful signal changes.

---

## 3. Feature Engineering

The notebook extracts complementary features from each physiological modality.

### Pupil Dynamics

Dynamic pupil behavior is characterized using:

* Maximum dilation rate
* Maximum constriction rate
* Mean pupil velocity
* Pupil velocity
* Pupil acceleration

These features capture rapid autonomic responses that may be associated with changes in arousal.

### GSR Features

* Mean tonic conductance
* Phasic peak count

### PPG Features

* Heart rate (HR)
* Heart-rate variability (RMSSD)

Trials are segmented into **20-second windows**, and feature vectors are computed for each trial.

**Total extracted trials:** **852**

---

## 4. Arousal Label Generation

An exploratory physiological arousal index is constructed by combining normalized GSR and heart-rate measures.

```text
Arousal Score =
Normalized GSR Peaks
+
Normalized Heart Rate
```

Trials are assigned to one of two classes:

* High Arousal
* Low Arousal

The resulting dataset is balanced:

| Class        | Samples |
| ------------ | ------- |
| Low Arousal  | 426     |
| High Arousal | 426     |

**Note:** Because the arousal labels are derived from physiological measurements rather than externally annotated ground truth, the classification results should be interpreted as prediction of a physiology-derived arousal index rather than independently validated psychological arousal.

---

# 🤖 Machine Learning

## Classification Model

A **Random Forest Classifier** is trained using multimodal physiological features.

Model inputs include:

* GSR tonic level
* GSR phasic peak count
* Heart rate
* HRV (RMSSD)
* Maximum pupil dilation rate
* Maximum pupil constriction rate
* Mean pupil velocity

To evaluate generalization across individuals, the notebook uses **Group K-Fold Cross-Validation**, ensuring that recordings from the same participant never appear in both training and testing sets.

---

## Hyperparameter Optimization

Model parameters are optimized using **GridSearchCV** with Group K-Fold validation.

Parameters explored include:

* Number of trees
* Maximum tree depth
* Minimum samples per split
* Feature selection strategy

### Best Configuration

| Parameter         | Value |
| ----------------- | ----- |
| n_estimators      | 100   |
| max_depth         | 10    |
| min_samples_split | 5     |
| max_features      | sqrt  |

---

# 📊 Results

## Multimodal Classification Performance

| Metric   | Performance |
| -------- | ----------- |
| Accuracy | 0.74        |
| ROC-AUC  | 0.83        |

### Optimized Model

Best cross-validated ROC-AUC:

**0.8626**

---

## Modality Comparison

| Model                   | Modalities                 | ROC-AUC    |
| ----------------------- | --------------------------- | ---------- |
| GSR Only                | GSR                          | ~0.78      |
| GSR + PPG               | GSR + HR + HRV               | ~0.83      |
| Full Model              | GSR + PPG + Pupil Dynamics   | ~0.83      |
| Optimized Random Forest | Full Model + Grid Search     | **0.8626** |

The results indicate that combining complementary physiological signals produces the strongest predictive performance.

---

# 📈 Feature Importance

The Random Forest model identifies the following variables as the most informative predictors:

| Rank | Feature                         |
| ---- | -------------------------------- |
| 1    | GSR Phasic Peak Count            |
| 2    | Heart Rate                       |
| 3    | Maximum Pupil Dilation Rate      |
| 4    | Maximum Pupil Constriction Rate  |
| 5    | Mean Pupil Velocity              |

GSR contributes the strongest predictive signal, while cardiovascular and pupil-dynamics features provide complementary physiological information.

---

# 📊 Generated Outputs

The notebook produces:

* Trial-wise multimodal feature matrix
* Physiological preprocessing outputs
* Random Forest classification results
* ROC curve
* Feature importance rankings
* Cross-validation performance metrics
* Hyperparameter optimization results

---

# 🧩 Key Findings

* Multimodal physiological signals successfully distinguish high and low arousal states.
* GSR provides the strongest individual predictor of arousal.
* Heart rate and HRV improve prediction by incorporating cardiovascular responses.
* Pupil dynamic features enrich the feature space and improve physiological characterization, although they provide smaller gains in overall classification performance.
* Subject-independent validation demonstrates that the model generalizes across participants.

---

# 🚀 Position Within the Project

This notebook extends the multimodal psychophysiology pipeline beyond eye movements by incorporating autonomic physiological responses.

Previous notebooks focused on:

* **Notebook 01:** Blink detection and EEG alpha analysis
* **Notebook 02:** Saccade latency and behavioral response analysis

The extracted GSR, PPG, and pupil-dynamics features are subsequently integrated into the multimodal fusion framework developed in **Notebook 04**.

---

# 🏁 Summary

This notebook presents a complete multimodal arousal prediction pipeline using pupil dynamics, GSR, and PPG signals from the OpenNeuro DS007537 dataset. The workflow combines physiological signal preprocessing, multimodal feature engineering, subject-independent machine learning, and hyperparameter optimization to evaluate physiology-derived arousal states. Together with the surrounding notebooks, it forms a key component of the end-to-end multimodal psychophysiology research pipeline.
