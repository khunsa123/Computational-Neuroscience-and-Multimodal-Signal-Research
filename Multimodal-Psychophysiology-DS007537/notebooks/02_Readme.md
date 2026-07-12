# 📄 02 — Saccade Latency & Decision Making (DS007537)
### Multimodal Psychophysiology — Eye Movements + Smartphone Interaction Behavior

> 📂 Part of [Multimodal-Psychophysiology-DS007537](../) · Notebook: [`02_saccade_latency_decision_making.ipynb`](./02_saccade_latency_decision_making.ipynb)

---

## ⭐ Overview

This notebook performs a full-cohort multimodal analysis of saccade latency (eye movement initiation time) and manual decision-making latency (smartphone touch reaction time) using the OpenNeuro dataset **DS007537**.

The project scales to all **23 subjects**, streaming eye-tracking and behavioral data directly from S3 (RAM-friendly, Colab-friendly). It quantifies how quickly participants orient their gaze toward stimuli and how this relates to their manual responses.

---

## 🧠 Research Questions

1. How fast do participants initiate saccades after a stimulus?
2. Does saccade latency predict smartphone reaction time?
3. Do subjects differ significantly in their oculomotor response speed?
4. Which subjects show statistically meaningful differences?

---

## 📁 Dataset

**OpenNeuro DS007537**

- Eye tracking (1000 Hz → downsampled to 250 Hz)
- Smartphone interaction timestamps
- 23 subjects
- Fully BIDS-formatted

---

## 🔧 Pipeline Summary

### 1. Data Acquisition (S3 Streaming)

A custom streaming function loads only what's needed, avoiding the full dataset download:

- `*_physio.tsv.gz` (eye tracking)
- `*_events.tsv` (stimulus + touch events)

### 2. Eye-Tracking Preprocessing

**Downsampling**
- Original sampling: 1000 Hz
- Downsampled to: 250 Hz → reduces RAM + speeds processing

**Velocity-based Saccade Detection**

For each subject:
- Interpolate missing gaze coordinates
- Compute velocity: `v_t = sqrt((x_t − x_t−1)² + (y_t − y_t−1)²) / dt`
- Threshold: 40 px/s
- Identify saccade onset as the first sample exceeding threshold
- Extract saccade onset times for trial alignment

**Output:** A list of saccade onset times per subject.

### 3. Trial Alignment

Using `events.tsv`:
- For each stimulus onset, find the first saccade occurring after it
- Compute saccade latency: `latency = t_saccade − t_stimulus`
- Extract touch reaction time from smartphone interaction events

**Full Cohort Output:**
> 📌 **792 aligned trials** · 📌 **23 subjects fully processed**

---

## 📊 Results & Visualizations

### 1. Saccade Latency Distribution

| Metric | Value |
|---|---|
| Mean latency | 0.058 s |
| Std | 0.0548 |
| Range | 0.0007 – 0.579 s |

Distribution is right-skewed (typical for reaction times).

📈 Saved as: `group_latency_dist.png`

### 2. Subject-wise Latency Variability

A boxplot shows clear inter-subject differences:
- Some subjects consistently initiate saccades faster
- Others show broader variability
- Indicates individual differences in oculomotor control

📈 Saved as: `intersubject_latency_boxplot.png`

### 3. Pairwise Statistical Tests

**T-Test (sub-01 vs sub-23)**

| Metric | Value |
|---|---|
| Mean latency sub-01 | 0.0694 s |
| Mean latency sub-23 | 0.0652 s |
| p-value | 0.8246 (no significant difference) |

**One-Way ANOVA (23 subjects)**

| Metric | Value |
|---|---|
| F | 2.4734 |
| p | 2.09e-4 (significant differences exist across subjects) |

**Tukey HSD Post-hoc**

Significant pairwise differences (p < 0.05):

| Subject A | Subject B | Mean Diff (s) | p-adj |
|---|---|---|---|
| sub-08 | sub-10 | −0.0564 | 0.0016 |
| sub-08 | sub-13 | −0.0530 | 0.0066 |
| sub-08 | sub-15 | −0.0486 | 0.0248 |
| sub-10 | sub-17 | 0.0526 | 0.0060 |
| sub-13 | sub-17 | 0.0491 | 0.0210 |

**Interpretation:**
- sub-08 consistently shows faster saccades
- sub-10, sub-13, sub-15, sub-17 show slower responses
- Confirms meaningful inter-subject variability

**Pairwise Heatmap**

A full matrix of mean differences with significance markers (*) is saved as: `saccade_latency_heatmap.png`

---

## 🧩 Decision-Making Analysis (Linear Regression)

**Model:**

```
Touch RT = 0.999 − 0.015 · Latency
R² = 0.0002
```

**Interpretation:**
- Saccade latency does **not** predict smartphone reaction time
- Eye movement initiation and manual response appear independent in this task
- Likely due to: task structure, smartphone interaction delays, motor execution variability

📈 Scatter plot with global regression line saved as: `group_decision_regression.png`

---

## 🧠 Interpretation & Insights

- ✔ **Saccade latency is fast and consistent** — mean latency ~58 ms aligns with typical human oculomotor response times.
- ✔ **Strong inter-subject variability** — ANOVA + Tukey HSD show meaningful differences across participants.
- ✔ **Saccade latency does not predict touch reaction time** — manual responses are slower (~1.0 s) and influenced by different cognitive/motor processes.
- ✔ **Multimodal alignment works robustly** — the pipeline successfully synchronizes eye movements and smartphone interactions across all subjects.

---

## 🚀 Next Notebooks

- **03 — Pupil Dilation + Stress/Arousal** — Combine pupil dilation with GSR + PPG to model arousal.
- **04 — Multimodal Fusion Model** — Fuse EEG + eye tracking + GSR + PPG for cognitive load classification.
- **05 — EEG + Eye Tracking Synchronization** — Align multimodal signals precisely using timestamps + drift correction.

---

## 🏁 Summary

This notebook establishes a complete multimodal behavioral pipeline: velocity-based saccade detection, trial-wise latency extraction, smartphone reaction time alignment, cohort-level statistical modeling (ANOVA + Tukey HSD), and linear regression decision-making analysis. It forms the second major component of the multimodal psychophysiology research suite.

---

📧 khunsaiftikhar123@gmail.com
