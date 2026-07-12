# 📄 03 — Pupil Dilation, Stress & Arousal (DS007537)
### Multimodal Physiological Analysis & Arousal Prediction — Pupil Dilation + GSR + PPG + Pupil Dynamics + ML Classification

> 📂 Part of [Multimodal-Psychophysiology-DS007537](../) · Notebook: [`03_pupil_dilation_stress_arousal.ipynb`](./03_pupil_dilation_stress_arousal.ipynb)

---

## ⭐ Overview

This notebook builds a full multimodal arousal-prediction pipeline using physiological signals from the OpenNeuro dataset **DS007537**. It integrates pupil dilation, GSR, PPG, and pupil dynamics to classify psychophysiological arousal states across **23 subjects**.

The pipeline is fully Colab-friendly, RAM-efficient, and S3-streamed, requiring no local dataset downloads.

---

## 🧠 Research Questions

1. Can multimodal physiological signals predict arousal?
2. Which modalities contribute most (GSR, PPG, pupil dynamics)?
3. Does subject-independent ML generalize across the cohort?
4. Does adding pupil dynamics improve prediction accuracy?

---

## 📁 Dataset

**OpenNeuro DS007537**

- Pupil diameter (left/right eyes)
- GSR (skin conductance)
- PPG (photoplethysmogram → HR + HRV)
- Smartphone interaction task
- 23 subjects
- Fully BIDS-formatted

---

## 🔧 Pipeline Summary

### 1. Multimodal Data Streaming (S3)

A custom loader streams `*_physio.tsv.gz` (eye tracking + GSR + PPG) and automatically identifies the correct columns for each modality:

| Modality | Column | Type |
|---|---|---|
| Pupil | `value` | `pd` |
| GSR | `x_coordinate` | `gy` |
| PPG | `value` | `sig` |

**Time Synchronization:** All signals are resampled to a common 10 Hz timeline, producing `pupil_size`, `gsr`, `ppg`, and `time` (0 → end).

### 2. Preprocessing

- **Blink Interpolation** — pupil values ≤ 0 or NaN interpolated for smooth dilation curves
- **Low-Pass Filtering** — Butterworth filter, 2 Hz cutoff, applied to GSR & PPG to remove high-frequency noise
- **Z-Scoring** — each modality normalized (`pupil_size_z`, `gsr_filt_z`, `ppg_filt_z`)
- **Baseline Correction** — rolling baseline (200 ms window): `Δpupil = pupil − baseline`
- **Smoothing** — 5-sample moving average → `pupil_smoothed`

### 3. Pupil Dynamics (New Feature Set)

The notebook introduces pupil velocity & acceleration features that capture rapid dilation/constriction, strongly linked to arousal:

- `pupil_velocity`
- `pupil_acceleration`
- `pupil_max_dilation_rate`
- `pupil_max_constriction_rate`
- `pupil_mean_velocity`

### 4. Trial-wise Feature Extraction

Trials are segmented into 20-second windows. For each trial, the pipeline extracts:

- **GSR features:** tonic level (baseline skin conductance), phasic peak count (rapid arousal spikes)
- **PPG features:** heart rate (HR), HRV (RMSSD)
- **Pupil dynamics:** max dilation rate, max constriction rate, mean velocity

> 📌 **Total trials extracted: 852**

### 5. Arousal Labeling

Arousal is defined using GSR + HR, normalized per subject to remove baseline differences:

```
arousal_score = norm(GSR peaks) + norm(HR)
```

Binary labels (High / Low arousal), balanced dataset:

| Label | Count |
|---|---|
| Low | 426 |
| High | 426 |

---

## 🤖 Machine Learning — Random Forest (Group-Aware CV)

### 6. Group K-Fold Cross-Validation

To ensure subject-independent generalization, the model uses `GroupKFold` (5 folds) with subject IDs as groups, preventing leakage across subjects.

**Features used (7 total):**
`gsr_tonic`, `gsr_phasic_peaks_count`, `heart_rate_bpm`, `hrv_rmssd`, `pupil_max_dilation_rate`, `pupil_max_constriction_rate`, `pupil_mean_velocity`

### 7. Model Performance

**Refined Multimodal Model (GSR + PPG + Pupil Dynamics)**

| Metric | Value |
|---|---|
| Accuracy | 0.74 |
| ROC-AUC | 0.83 |

**Comparison:**

| Model | Modalities | ROC-AUC |
|---|---|---|
| GSR Only | GSR | ~0.78 |
| GSR + PPG | GSR + HR + HRV | ~0.83 |
| Full Model | GSR + PPG + Pupil Dynamics | 0.83 |

Pupil dynamics did not increase AUC, but improved feature diversity and trial-level robustness.

---

## 🔍 Feature Importance

**Top predictors:**
1. GSR phasic peak count
2. Heart rate (PPG)
3. Pupil dilation/constriction rates

**Interpretation:**
- GSR remains the strongest arousal indicator
- PPG adds cardiovascular arousal signal
- Pupil dynamics contribute meaningful but smaller effects

---

## 🔧 Hyperparameter Optimization (Grid Search)

`GridSearchCV` + `GroupKFold` tested:

- `n_estimators`: 50, 100, 200
- `max_depth`: None, 10, 20
- `min_samples_split`: 2, 5, 10
- `max_features`: sqrt, log2

**Best Parameters:**

```python
{
  'max_depth': 10,
  'max_features': 'sqrt',
  'min_samples_split': 5,
  'n_estimators': 100
}
```

> 📌 **Best cross-validated ROC-AUC: 0.8626** — the best model for the dataset so far.

---

## 🧠 Interpretation & Insights

- ✔ **Arousal is best predicted by GSR + HR** — consistent with psychophysiology literature.
- ✔ **Pupil dynamics add nuance** — they capture rapid dilation/constriction linked to arousal.
- ✔ **Subject-independent ML works** — GroupKFold ensures generalization across individuals.
- ✔ **Hyperparameter tuning improves performance** — AUC increased to 0.8626, the highest so far.

---

## 🚀 Next Notebooks

- **04 — Multimodal Fusion Model** — Combine EEG + eye tracking + GSR + PPG + pupil dynamics for cognitive load classification.
- **05 — EEG + Eye Tracking Synchronization** — Align multimodal signals precisely using timestamps + drift correction.

---

## 🏁 Summary

This notebook establishes a complete multimodal arousal-prediction pipeline: S3 streaming, multimodal synchronization, blink interpolation, low-pass filtering, z-scoring, pupil dynamics, GSR + HR + HRV extraction, subject-independent ML, and hyperparameter tuning. It forms the third major component of the multimodal psychophysiology research suite.

---

📧 khunsaiftikhar123@gmail.com
