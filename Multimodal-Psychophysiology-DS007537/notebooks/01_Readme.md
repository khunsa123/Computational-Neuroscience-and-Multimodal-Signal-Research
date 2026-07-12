# 📄 01 — Blink Detection + Cognitive Load (DS007537)
### Multimodal Psychophysiology — Eye Tracking + EEG Alpha Power

> 📂 Part of [Multimodal-Psychophysiology-DS007537](../) · Notebook: [`01_blink_detection_cognitive_load.ipynb`](./01_blink_detection_cognitive_load.ipynb)

---

## ⭐ Overview

This notebook performs a multimodal cognitive-load analysis using eye-tracking and EEG data from the OpenNeuro dataset **DS007537**. The goal is to quantify how blink behavior relates to neural alpha-band activity, and whether these physiological markers can classify cognitive load.

The pipeline processes all **23 subjects**, streaming data directly from the OpenNeuro S3 bucket (RAM-friendly, Colab-friendly).

---

## 🧠 Research Questions

1. Do blink rates correlate with EEG alpha power?
2. Can blink behavior + alpha power classify cognitive load?
3. Are these relationships consistent across subjects?

---

## 📁 Dataset

**OpenNeuro DS007537**

- 66-channel EEG (1000 Hz)
- Head-mounted eye tracking
- GSR + PPG *(not used in this notebook)*
- Smartphone interaction task
- 23 subjects
- Fully BIDS-formatted

---

## 🔧 Pipeline Summary

### 1. Data Acquisition (S3 Streaming)

A custom downloader streams only the required files, avoiding the full 6.1 GB dataset download:

- `*_eeg.vhdr`, `*_eeg.eeg`, `*_eeg.vmrk`
- `*_physio.tsv.gz` (eye tracking)
- `*_events.tsv` (trial markers)

### 2. Eye-Tracking Preprocessing

**Function:** `preprocess_and_detect_blinks_v3(df)`

**Steps:**
- Filter pupil diameter samples (`type == 'pd'`)
- Merge duplicate timestamps (averaging left/right eye)
- Convert timestamps from microseconds → seconds
- **Blink detection:**
  - Pupil ≤ 0.1 or NaN → dropout
  - Identify blink start/end using diff
  - Keep only physiological durations: 50–500 ms

**Outputs:**
- Cleaned pupil time series
- Blink event table (`start_sec`, `duration_sec`)

### 3. EEG Alpha Power Extraction

**Function:** `process_eeg_alpha(vhdr_path)`

**Steps:**
- Load BrainVision EEG
- Pick EEG channels
- Bandpass filter: 8–12 Hz (alpha band)
- Hilbert transform → envelope
- Downsample to 10 Hz (RAM-friendly)
- Compute global alpha power (mean across channels)

**Outputs:**
- `avg_alpha_power` (1D time series)
- `times` (aligned timestamps)

### 4. Trial Segmentation

Using `*_events.tsv`:
- Extract trial windows between consecutive event onsets
- Compute:
  - Blink rate = blinks per minute
  - Mean alpha power within trial window

Across 23 subjects, the pipeline produced:

> 📌 **Total trials: 1406**

### 5. Statistical Analysis

**Group-level correlation:**

| Test | Value |
|---|---|
| Pearson | r = −0.011 (ns) |
| Spearman | ρ = 0.169, p < 1e-9 (significant) |

**Interpretation:**
- Blink rate and alpha power show a weak but significant monotonic relationship.
- Alpha power is more sensitive to cognitive load than blink rate.

**Subject-wise correlations:**
A faceted plot shows:
- Some subjects show strong positive/negative correlations
- Others show no relationship
- Indicates individual variability in psychophysiological coupling

### 6. Machine Learning — Cognitive Load Classification

**Labels:**
- High cognitive load = alpha power below median
- Low cognitive load = alpha power above median

**Features:** Blink rate, Alpha power

**Model:** Logistic Regression (70/30 train/test split, standardized features)

**Results — Accuracy: 86.26%**

| Class | Precision | Recall | F1 |
|---|---|---|---|
| Low Load | 1.00 | 0.73 | 0.84 |
| High Load | 0.78 | 1.00 | 0.88 |

**Feature Importance:**

| Feature | Coefficient | Importance |
|---|---|---|
| Alpha Power | −12.03 | ⭐ Highest |
| Blink Rate | −0.12 | Low |

**Interpretation:**
- Alpha power is the primary predictor of cognitive load.
- Blink rate adds small but useful information.

---

## 📊 Key Figures

The notebook generates:

- Group-level regression plot
- Subject-wise faceted correlation grid
- Confusion matrix
- ROC curve (AUC)
- Feature importance bar plot

---

## 🧩 Interpretation & Insights

- ✔ **Blink rate is a weak but reliable behavioral marker** — it correlates with alpha power across subjects, but not strongly.
- ✔ **Alpha power is a strong neural marker of cognitive load** — consistent with literature: alpha decreases with increased cognitive demand.
- ✔ **Multimodal ML classification works well** — even with only two features, the model reaches 86% accuracy.
- ✔ **Individual differences matter** — subject-wise plots show variability in blink–alpha coupling.

---

## 🚀 Next Notebooks

- **02 — Saccade Latency + Decision Making** — Use gaze velocity to detect saccades and relate them to smartphone interaction behavior.
- **03 — Pupil Dilation + Stress/Arousal** — Combine pupil dilation with GSR + PPG to model arousal.
- **04 — Multimodal Fusion Model** — Fuse EEG + eye tracking + GSR + PPG for cognitive load classification.
- **05 — EEG + Eye Tracking Synchronization** — Align multimodal signals precisely using timestamps + drift correction.

---

## 🏁 Summary

This notebook establishes a complete multimodal cognitive-load pipeline: blink detection, alpha power extraction, trial segmentation, correlation analysis, and machine learning classification. It forms the foundation for the remaining four multimodal projects.

---

📧 khunsaiftikhar123@gmail.com
