# 💪 EMG Stroke Recovery Monitoring

## 📌 Project Overview

This project presents a modular Python pipeline for **EMG (Electromyography) signal analysis applied to stroke recovery monitoring**. The system processes EMG recordings from both healthy and post-stroke individuals, extracts time-domain and frequency-domain features, and trains multiple classification models to distinguish between the two groups — providing a data-driven framework for objective stroke rehabilitation assessment.

---

## 🎯 Objectives

- Process and segment raw EMG signals from healthy and post-stroke subjects
- Extract discriminative time-domain and frequency-domain features from EMG windows
- Train and compare classical ML and deep learning classifiers for subject group classification
- Visualise and compare model performance for clinical interpretability

---

## 🧠 Methods & Techniques

- EMG signal loading, bandpass filtering, and segmentation into fixed-length windows
- **Feature extraction:**
  - Time-domain: RMS, MAV, zero crossing rate, waveform length, variance
  - Frequency-domain: mean frequency, median frequency, spectral power
- **Dual-input approach:**
  - SVM and MLP trained on extracted feature vectors
  - 1D-CNN trained directly on raw segmented EMG windows (end-to-end)
- Model comparison visualised as a performance bar chart

### 📊 Evaluation Metrics

- Accuracy
- Precision, Recall, F1-score
- Model comparison plot

---

## 🤖 Models Implemented

- **Support Vector Machine (SVM)** — classical ML baseline on extracted features
- **Multi-Layer Perceptron (MLP)** — shallow neural network on extracted features
- **1D Convolutional Neural Network (1D-CNN)** — end-to-end learning on raw EMG windows

---

## 📊 Dataset

- **EMG Reaching Dataset** — EMG recordings from healthy and post-stroke individuals during reaching tasks
- Dataset structure: `Health_reaching/` and `Stroke_reaching/` subject folders
- Each subject folder contains `Target *.csv` files with raw EMG channel data
- Update `--dataset-root` to match your local dataset path

---

## 🛠️ Tech Stack

- **Programming:** Python
- **Signal Processing:** NumPy, SciPy
- **ML / DL:** scikit-learn, TensorFlow / Keras
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Environment:** VS Code

---

## 📂 Project Structure

```
EMG-Stroke-Recovery-Monitoring/
│── main.py                             # Full pipeline entry point
│── requirements.txt                    # Python dependencies
│── emg_stroke_recovery_monitoring/
│   ├── data.py                         # EMG loading, filtering, segmentation
│   ├── features.py                     # Time & frequency domain feature extraction
│   ├── models.py                       # SVM, MLP, 1D-CNN definitions & training
│   ├── utils.py                        # Plotting and result visualisation
│   └── __init__.py                     # Package exports
└── README.md
```

---

## ⚙️ Installation & Usage

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full pipeline
python main.py --dataset-root "EMG_Reaching_Healthy_Stroke" --output model_comparison.png
```

> Set `--dataset-root` to the folder containing `Health_reaching` and `Stroke_reaching` if your dataset is stored elsewhere.

---

## ⚠️ Notes

- The 1D-CNN operates on raw segmented EMG windows; SVM and MLP use extracted feature vectors
- Each subject folder must contain `Target *.csv` files matching the original dataset layout
- Output comparison plot is saved as `model_comparison.png` by default

---

## 🚀 Future Work

- Extension to multi-session longitudinal tracking of stroke recovery progress
- Integration of additional EMG biomarkers (fatigue indices, co-contraction ratios)
- Multimodal fusion with EEG for combined neural and muscular activity analysis
- Real-time EMG classification pipeline for rehabilitation feedback systems

---

## 📬 Contact

**Khunsa Iftikhar**
📧 [khunsaiftikhar123@gmail.com](mailto:khunsaiftikhar123@gmail.com)
🔗 [linkedin.com/in/khunsa-iftikhar](https://www.linkedin.com/in/khunsa-iftikhar/)

---

⚠️ **Ethical Note:** All datasets used are publicly available, anonymised research datasets shared under open-access licenses for non-commercial research purposes.
