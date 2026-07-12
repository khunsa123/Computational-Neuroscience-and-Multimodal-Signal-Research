# 📄 01 — Blink Detection & Cognitive Load Analysis (DS007537)

### Eye Tracking + EEG Alpha Power • Blink Detection • Correlation Analysis • Logistic Regression
📂 **Part of:** *Multimodal Psychophysiology Pipeline — DS007537*
📓 **Notebook:** `01_blink_detection_cognitive_load.ipynb`

---

# ⭐ Overview
This notebook establishes the first stage of the **Multimodal Psychophysiology Pipeline** by combining **eye-tracking** and **EEG** data to investigate the relationship between blink behavior and neural activity associated with cognitive load.

The workflow performs blink detection from pupil recordings, extracts EEG alpha-band power, aligns both modalities with experimental trials, and evaluates their relationship using statistical analysis and machine learning.

Designed for **Google Colab**, the notebook streams data directly from the **OpenNeuro DS007537** dataset, processes participants individually to minimize memory usage, and follows a modular, BIDS-compatible workflow.

---

# 🧠 Research Questions
This notebook investigates the following questions:

1. Does blink rate correlate with EEG alpha-band activity?
2. Can blink behavior and EEG alpha power distinguish different levels of cognitive load?
3. How consistent is the blink–alpha relationship across participants?

---

# 📁 Dataset
**OpenNeuro DS007537**

The notebook analyzes recordings from **23 participants**, including:

- 66-channel EEG (1000 Hz)
- Head-mounted eye tracking
- Experimental event markers
- Fully BIDS-compliant organization
Although the dataset also includes GSR and PPG recordings, those modalities are explored in later notebooks.

---

# 🔧 Pipeline Overview
The analysis consists of five major stages.

---

## 1. Data Acquisition
The notebook streams only the files required for blink detection and EEG analysis.

Required files include:

- `*_eeg.vhdr`
- `*_eeg.eeg`
- `*_eeg.vmrk`
- `*_physio.tsv.gz`
- `*_events.tsv`
Streaming minimizes storage requirements and enables efficient execution in cloud-based environments such as Google Colab.

---

## 2. Eye-Tracking Preprocessing
Pupil recordings are processed to identify blink events.

Processing steps include:

- Selection of pupil diameter samples
- Merging left and right eye measurements
- Timestamp conversion
- Missing-value handling
- Blink detection using pupil dropouts
- Physiological duration filtering (50–500 ms)
The pipeline produces:

- Cleaned pupil time series
- Blink event table
- Blink durations
- Blink timestamps

---

## 3. EEG Processing
EEG recordings are processed using **MNE-Python**.

Processing includes:

- BrainVision file loading
- EEG channel selection
- Alpha-band filtering (8–12 Hz)
- Hilbert envelope computation
- Temporal downsampling
- Global alpha-power estimation
The resulting alpha-power time series is synchronized with experimental events for trial-wise analysis.

---

## 4. Trial Segmentation
Experimental event markers are used to divide recordings into individual trials.

For each trial, the notebook computes:

- Blink rate
- Mean EEG alpha power
**Total analyzed trials:** **1,406**

The resulting trial-level feature table forms the basis for statistical analysis and classification.

---

## 5. Statistical Analysis
The relationship between blink rate and EEG alpha power is evaluated using both linear and rank-based correlation analyses.

### Pearson Correlation
StatisticValueCorrelation (r)−0.011No meaningful linear relationship was observed across the cohort.

---

### Spearman Correlation
StatisticValueCorrelation (ρ)0.169p-value< 1 × 10⁻⁹The significant Spearman correlation suggests a weak monotonic association between blink rate and alpha-band activity.

Subject-level analyses further demonstrate substantial variability in blink–alpha relationships across participants.

---

# 🤖 Machine Learning

## Classification Model
A **Logistic Regression** classifier is trained using:

- Blink rate
- Mean EEG alpha power
The dataset is divided into training and testing sets using a **70/30 split**, with feature standardization applied prior to model fitting.

### Cognitive Load Labeling
An exploratory cognitive-load index is derived from trial-wise EEG alpha power:

- **High cognitive load:** Alpha power below the median
- **Low cognitive load:** Alpha power above the median
**Note:** Because the cognitive-load labels are derived from EEG alpha power, and alpha power is also included as an input feature, the reported classification performance should be interpreted as prediction of an EEG-derived cognitive-load index rather than an independently annotated cognitive state.

---

# 📊 Results

## Classification Performance
MetricValueAccuracy**86.26%**
### Class-wise Performance
ClassPrecisionRecallF1-scoreLow Load1.000.730.84High Load0.781.000.88
---

## Feature Importance
FeatureRelative ContributionEEG Alpha PowerHighestBlink RateLower but complementaryThe results indicate that EEG alpha power provides the strongest predictive signal, while blink rate contributes additional behavioral information.

---

# 📈 Generated Outputs
The notebook generates:

- Trial-wise blink feature table
- EEG alpha-power time series
- Correlation analyses
- Subject-wise correlation plots
- Logistic regression results
- Confusion matrix
- ROC curve
- Feature importance visualization
Representative visualizations include:

- Group-level regression plot
- Subject-wise correlation grid
- Confusion matrix
- ROC curve
- Feature importance plot

---

# 🧩 Key Findings

- Blink rate exhibits a weak but statistically significant association with EEG alpha activity across the cohort.
- EEG alpha power provides a stronger indicator of the physiology-derived cognitive-load index than blink rate alone.
- Combining neural and behavioral features improves classification compared with using blink behavior independently.
- Subject-level analyses reveal considerable variability in blink–alpha coupling, highlighting individual differences in psychophysiological responses.
- The notebook establishes a reusable workflow for multimodal feature extraction that supports subsequent analyses within the project.

---

# 🚀 Position Within the Project
This notebook introduces the multimodal psychophysiology pipeline by combining eye-tracking and EEG analyses.

Project progression:

- **Notebook 01:** Blink detection and EEG alpha analysis
- **Notebook 02:** Saccade latency and behavioral response analysis
- **Notebook 03:** Multimodal physiological arousal prediction
- **Notebook 04:** Multimodal cognitive load fusion
- **Notebook 05:** EEG and eye-tracking synchronization
The extracted blink features and EEG spectral measures provide foundational components for the multimodal fusion models developed in later notebooks.

---

# 🏁 Summary
This notebook presents a complete pipeline for blink detection and EEG alpha-band analysis using the OpenNeuro DS007537 dataset. The workflow combines eye-tracking preprocessing, EEG spectral feature extraction, trial-wise synchronization, statistical correlation analysis, and logistic regression to explore relationships between behavioral and neural indicators of cognitive load. As the first notebook in the series, it establishes the core multimodal processing framework that is progressively extended throughout the remaining projects.
