# 📄 02 — Saccade Latency & Decision-Making Analysis (DS007537)

### Eye Tracking • Saccade Detection • Smartphone Reaction Time • Statistical Analysis
📂 **Part of:** *Multimodal Psychophysiology Pipeline — DS007537*
📓 **Notebook:** `02_saccade_latency_decision_making.ipynb`

---

# ⭐ Overview
This notebook investigates the relationship between **saccadic eye movements** and **behavioral response timing** using eye-tracking and smartphone interaction data from the **OpenNeuro DS007537** dataset.

The workflow performs velocity-based saccade detection, stimulus-locked trial alignment, latency extraction, and cohort-level statistical analyses to examine individual differences in oculomotor behavior and their relationship to manual responses.

Designed for **Google Colab**, the notebook streams data directly from OpenNeuro, processes participants individually to minimize memory usage, and follows a modular, BIDS-compatible workflow.

---

# 🧠 Research Questions
This notebook investigates the following questions:

1. How quickly do participants initiate saccadic eye movements following stimulus presentation?
2. Is saccade latency associated with smartphone touch reaction time?
3. How much variability exists in saccade latency across participants?
4. Which participants exhibit statistically significant differences in oculomotor response speed?

---

# 📁 Dataset
**OpenNeuro DS007537**

The notebook analyzes recordings from **23 participants**, including:

- Head-mounted eye tracking
- Smartphone interaction events
- Experimental event markers
- Fully BIDS-compliant organization
Eye-tracking recordings are originally sampled at **1000 Hz** and downsampled to **250 Hz** to improve computational efficiency while preserving temporal resolution for saccade detection.

---

# 🔧 Pipeline Overview
The analysis consists of four major stages.

---

## 1. Data Acquisition
The notebook streams only the files required for eye-tracking and behavioral analysis.

Required files include:

- `*_physio.tsv.gz`
- `*_events.tsv`
Streaming avoids downloading the complete dataset, making the workflow suitable for cloud-based environments such as Google Colab.

---

## 2. Eye-Tracking Preprocessing
Raw gaze recordings undergo preprocessing prior to saccade detection.

Processing steps include:

- Downsampling from 1000 Hz to 250 Hz
- Missing-value interpolation
- Gaze coordinate cleaning
- Time normalization
Velocity is then computed from consecutive gaze samples using the Euclidean displacement between gaze positions.

---

## 3. Velocity-Based Saccade Detection
Saccades are identified using a velocity thresholding approach.

For each participant, the pipeline:

- Computes gaze velocity
- Detects threshold crossings
- Identifies saccade onset
- Records saccade timestamps
A velocity threshold of **40 px/s** is used to identify rapid eye movements while suppressing small fixation-related fluctuations.

---

## 4. Trial Alignment
Saccade events are aligned with experimental stimuli using the event markers provided in the dataset.

For each trial, the notebook extracts:

- Stimulus onset
- First saccade following stimulus presentation
- Smartphone touch response
Saccade latency is calculated as:

```
Saccade Latency = Saccade Onset − Stimulus Onset
```
Touch reaction time is obtained from the corresponding behavioral event timestamps.

**Total aligned trials:** **792**

---

# 📊 Statistical Analysis
The synchronized trial dataset is analyzed using several complementary statistical methods.

### Descriptive Statistics
Overall latency distribution is summarized using:

- Mean
- Standard deviation
- Range

### Group Comparisons
Inter-subject variability is evaluated using:

- Independent t-test
- One-way ANOVA
- Tukey HSD post-hoc comparisons

### Behavioral Association
Linear regression is performed to examine whether saccade latency is associated with smartphone touch reaction time.

---

# 📊 Results

## Saccade Latency Distribution
MetricValueMean0.058 sStandard Deviation0.0548 sRange0.0007–0.579 sThe latency distribution is positively skewed, consistent with the variability commonly observed in reaction-time measurements.

---

## Inter-Subject Variability

### Independent t-Test
Comparisonp-valuesub-01 vs. sub-230.8246No statistically significant difference was observed between these two participants.

---

### One-Way ANOVA
StatisticValueF2.4734p-value2.09 × 10⁻⁴The ANOVA indicates significant differences in saccade latency across the participant cohort.

---

### Tukey HSD
Post-hoc comparisons identify several participant pairs with statistically significant latency differences, demonstrating substantial inter-individual variability in oculomotor response timing.

---

## Behavioral Regression
Linear regression between saccade latency and smartphone touch reaction time produced:

```
Touch Reaction Time
=
0.999 − 0.015 × Saccade Latency
```
**Coefficient of determination (R²):**

**0.0002**

The results indicate that saccade latency explains very little variation in manual response time within this experimental task.

---

# 📈 Generated Outputs
The notebook generates:

- Saccade latency distributions
- Inter-subject boxplots
- Pairwise significance heatmaps
- Regression plots
- Statistical summary tables
- Trial-wise latency dataset
Representative figures include:

- `group_latency_dist.png`
- `intersubject_latency_boxplot.png`
- `saccade_latency_heatmap.png`
- `group_decision_regression.png`

---

# 🧩 Key Findings

- Mean saccade latency across the cohort is approximately **58 ms**.
- Significant variability exists in oculomotor response timing between participants.
- Several participant pairs exhibit statistically significant latency differences following Tukey HSD analysis.
- Saccade latency shows little association with smartphone touch reaction time, suggesting that eye-movement initiation and manual responses reflect different stages of task performance.
- The synchronization pipeline successfully aligns eye-tracking and behavioral events for large-scale cohort analysis.

---

# 🚀 Position Within the Project
This notebook extends the multimodal psychophysiology pipeline by focusing on dynamic eye-movement behavior.

Project progression:

- **Notebook 01:** Blink detection and EEG alpha analysis
- **Notebook 02:** Saccade latency and behavioral response analysis
- **Notebook 03:** Multimodal physiological arousal prediction
- **Notebook 04:** Multimodal cognitive load fusion
- **Notebook 05:** EEG and eye-tracking synchronization
The extracted behavioral timing measures complement the physiological features developed in the later multimodal analyses.

---

# 🏁 Summary
This notebook presents a complete pipeline for saccade detection and behavioral latency analysis using eye-tracking and smartphone interaction data from the OpenNeuro DS007537 dataset. The workflow combines velocity-based saccade detection, stimulus-locked trial alignment, cohort-level statistical analysis, and regression modeling to characterize oculomotor behavior across participants. Together with the other notebooks in the project, it contributes to a comprehensive multimodal framework for psychophysiological signal analysis and human–computer interaction research.
