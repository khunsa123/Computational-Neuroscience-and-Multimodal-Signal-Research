# 📄 README — Project 5: Multimodal Synchronization Pipeline (EEG + Eye-Tracking)

### Stimulus-Locked Alignment • Drift Correction • Multimodal Epoching • Cross-Modal Analysis

## ⭐ Overview
This notebook implements a complete multimodal synchronization pipeline for aligning EEG and eye-tracking signals from the OpenNeuro dataset DS007537.

It is the most technically advanced notebook in the series, demonstrating:

- Clock drift correction
- Stimulus-locked multimodal epoching
- Joint EEG + gaze + pupil analysis
- Cohort-level statistical modeling
- Cross-modal regressions and effect size estimation

This pipeline is essential for neurophysiology, HCI, and NeuroAI research requiring precise multimodal alignment.

## 🧠 Research Questions
1. Can EEG and eye-tracking be synchronized accurately across 23 subjects?
2. Do gaze trajectories differ across stimulus categories?
3. Does pupil dilation correlate with EEG alpha power?
4. What multimodal features show the strongest stimulus-locked effects?

## 📁 Dataset
OpenNeuro DS007537

- 64-channel EEG (BrainVision)
- Eye tracking (pupil diameter + gaze vectors)
- Smartphone interaction task
- 23 subjects
- Fully BIDS-formatted

## 🔧 Pipeline Summary

### 1. Full Dataset Acquisition (AWS S3 Sync)
The notebook downloads the dataset using AWS S3 sync so that EEG, eye-tracking, event markers, and metadata are all available for analysis.

### 2. EEG Loading and Event Extraction
Using MNE, the pipeline:

- Loads BrainVision EEG files
- Extracts stimulus annotations
- Converts event markers into sample-accurate timestamps
- Prepares epochs from -200 ms to +800 ms around each stimulus

### 3. Eye-Tracking Loading and Trigger Detection
Eye-tracking files contain:

- Pupil diameter
- Gaze direction
- Raw timestamps
- Trigger pulses

Triggers are used to align eye-tracking time with EEG time.

### 4. Linear Drift Correction
The EEG and eye-tracking systems run on independent clocks, causing drift. The pipeline computes a linear correction between modalities using shared triggers, enabling millisecond-level alignment.

### 5. Multimodal Epoch Extraction
For each trial, the notebook extracts:

- EEG segments around the stimulus
- Synchronized eye-tracking segments
- Alpha power envelope
- Mean pupil diameter
- Mean gaze X/Y coordinates

## 📊 Results and Visualizations

### 1. Subject-Level Summary Table
For each subject, the pipeline summarizes:

- Mean alpha power
- Mean pupil size
- Mean gaze X/Y
- Total synchronized trials

### 2. Synchronization Verification
The notebook displays drift slope, offset, and synchronized timestamps to confirm successful alignment.

### 3. Multimodal Trial Visualization
Sample trials show EEG alpha envelope, gaze trajectories, and pupil dilation curves to verify temporal alignment.

### 4. Gaze Differences Across Stimulus Types
Statistical comparisons of gaze positions across stimulus categories reveal strong stimulus-dependent effects.

### 5. Pupil Dilation Differences
Pupil-size comparisons show variable and often non-significant differences across trials.

### 6. EEG Alpha Differences Across Stimuli
Alpha-power comparisons indicate stimulus-related modulation, though effects may vary by subject.

### 7. Cross-Modal Regression
Regression analyses test the relationship between subject-level alpha power and pupil size.

### 8. Gaze X/Y Correlation
Correlation analysis shows a weak but highly significant relationship between gaze X and Y movements.

### 9. Power Analysis
Effect-size estimates support the idea that relatively small trial counts can be sufficient to detect strong effects.

## 🧠 Interpretation and Insights
- Synchronization works reliably across subjects
- Gaze trajectories show strong stimulus-locked effects
- Pupil dilation is more variable and less consistently stimulus-locked
- Alpha power shows stimulus-dependent trends
- Cross-modal relationships vary across subjects
- Multimodal epoching enables rich downstream analyses

## 🚀 Future Work
This synchronization pipeline enables:

- Joint EEG-gaze decoding models
- Multimodal RNN and Transformer architectures
- Time-locked multimodal fusion
- Neural correlates of saccades and pupil dilation
- Cross-subject multimodal generalization

## 🏁 Summary
This notebook establishes a complete multimodal synchronization pipeline covering dataset acquisition, EEG and eye-tracking alignment, drift correction, stimulus-locked epoching, multimodal feature extraction, statistical analysis, effect size estimation, and cross-modal regression. It forms the fifth and final component of the multimodal psychophysiology research suite.
