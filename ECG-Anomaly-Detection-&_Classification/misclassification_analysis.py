import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

import config


def compare_autoencoder_vs_classifier_misclassifications(
    normal_data_autoencoder,
    abnormal_data_autoencoder,
    mse_normal,
    mse_abnormal,
    threshold,
    X_test_df,
    y_test_series,
    y_pred_rf_array,
    df_balanced
):
    print('Comparing autoencoder and classifier misclassifications...')

    predicted_labels_normal = (mse_normal > threshold).astype(int)
    autoencoder_fp_indices = normal_data_autoencoder.iloc[np.where(predicted_labels_normal == 1)[0]].index

    predicted_labels_abnormal = (mse_abnormal > threshold).astype(int)
    autoencoder_fn_indices = abnormal_data_autoencoder.iloc[np.where(predicted_labels_abnormal == 0)[0]].index

    rf_misclassified_indices = X_test_df.iloc[np.where(y_test_series != y_pred_rf_array)[0]].index

    print(f'Autoencoder false positives: {len(autoencoder_fp_indices)}')
    print(f'Autoencoder false negatives: {len(autoencoder_fn_indices)}')
    print(f'RF misclassifications: {len(rf_misclassified_indices)}')

    if len(rf_misclassified_indices) > 0:
        num_samples_to_plot = min(5, len(rf_misclassified_indices))
        misclassified_samples = df_balanced.loc[rf_misclassified_indices].drop(columns=['label']).head(num_samples_to_plot)
        true_labels = df_balanced.loc[rf_misclassified_indices]['label'].head(num_samples_to_plot)
        predicted_labels = y_pred_rf_array[np.where(y_test_series != y_pred_rf_array)[0]][:num_samples_to_plot]

        fig, axes = plt.subplots(num_samples_to_plot, 1, figsize=(12, num_samples_to_plot * 3))
        if num_samples_to_plot == 1:
            axes = [axes]

        fig.suptitle('Samples Misclassified by RandomForestClassifier', fontsize=16)

        for i in range(num_samples_to_plot):
            ax = axes[i]
            ax.plot(misclassified_samples.iloc[i].values)
            ax.set_title(f'Sample {misclassified_samples.index[i]} - True: {true_labels.iloc[i]}, Predicted: {predicted_labels[i]}')
            ax.set_xlabel('Time Points')
            ax.set_ylabel('Scaled ECG Reading')
            ax.grid(True)

        plt.tight_layout(rect=[0, 0.03, 1, 0.96])
        plt.show()
    else:
        print('No RF misclassified samples found in the test set.')

    return rf_misclassified_indices


def find_and_analyze_common_supervised_misclassifications(
    X_test,
    y_test,
    y_pred_rf,
    y_pred_gbc,
    y_pred_svm,
    best_rf_classifier,
    gbc_classifier,
    svm_classifier
):
    print('Finding commonly misclassified samples across supervised models...')

    rf_misclassified_indices = X_test[y_test != y_pred_rf].index.tolist()
    gbc_misclassified_indices = X_test[y_test != y_pred_gbc].index.tolist()
    svm_misclassified_indices = X_test[y_test != y_pred_svm].index.tolist()

    common_misclassified_indices = list(set(rf_misclassified_indices) & set(gbc_misclassified_indices) & set(svm_misclassified_indices))

    print(f'RF misclassified: {len(rf_misclassified_indices)}')
    print(f'GBC misclassified: {len(gbc_misclassified_indices)}')
    print(f'SVM misclassified: {len(svm_misclassified_indices)}')
    print(f'Commonly misclassified: {len(common_misclassified_indices)}')

    common_misclassified_data = pd.DataFrame()
    if common_misclassified_indices:
        common_misclassified_data = X_test.loc[common_misclassified_indices]
        common_true_labels = y_test.loc[common_misclassified_indices]

        common_pred_rf = best_rf_classifier.predict(common_misclassified_data)
        common_pred_gbc = gbc_classifier.predict(common_misclassified_data)
        common_pred_svm = svm_classifier.predict(common_misclassified_data)

        summary = pd.DataFrame({
            'True Label': common_true_labels,
            'RF Predicted': common_pred_rf,
            'GBC Predicted': common_pred_gbc,
            'SVM Predicted': common_pred_svm
        }, index=common_misclassified_indices)

        print(summary)

        num_samples = min(5, len(common_misclassified_indices))
        fig, axes = plt.subplots(num_samples, 1, figsize=(12, num_samples * 3))
        if num_samples == 1:
            axes = [axes]

        fig.suptitle('Commonly Misclassified Samples by All Models', fontsize=16)

        for i, idx in enumerate(common_misclassified_indices[:num_samples]):
            ax = axes[i]
            ax.plot(common_misclassified_data.loc[idx].values)
            ax.set_title(
                f'Sample {idx} - True: {common_true_labels.loc[idx]}, RF: {common_pred_rf[i]}, GBC: {common_pred_gbc[i]}, SVM: {common_pred_svm[i]}'
            )
            ax.set_xlabel('Time Points')
            ax.set_ylabel('Scaled ECG Reading')
            ax.grid(True)

        plt.tight_layout(rect=[0, 0.03, 1, 0.96])
        plt.show()
    else:
        print('No common misclassifications found.')

    return common_misclassified_data, common_misclassified_indices


def compare_common_misclassified_to_average_correct(common_misclassified_data, X_test, y_test, y_pred_tuned):
    print('Comparing misclassified samples to average correctly classified abnormal ECGs...')

    correct_abnormal_mask = (y_test == 1) & (y_pred_tuned == 1)
    correctly_classified_abnormal_data = X_test[correct_abnormal_mask]
    average_abnormal_waveform = correctly_classified_abnormal_data.mean(axis=0)

    print(f'Correctly classified abnormal samples: {len(correctly_classified_abnormal_data)}')

    if not common_misclassified_data.empty:
        num_samples = min(5, len(common_misclassified_data))
        fig, axes = plt.subplots(num_samples, 1, figsize=(12, num_samples * 3))
        if num_samples == 1:
            axes = [axes]

        fig.suptitle('Misclassified vs. Average Correct Abnormal ECG', fontsize=16)

        for i, idx in enumerate(common_misclassified_data.index[:num_samples]):
            ax = axes[i]
            ax.plot(common_misclassified_data.loc[idx].values, label='Misclassified Sample', color='red')
            ax.plot(average_abnormal_waveform.values, label='Average Correct Abnormal', color='blue', linestyle='--')
            ax.set_title(f'Sample {idx}')
            ax.set_xlabel('Time Points')
            ax.set_ylabel('Scaled ECG Reading')
            ax.legend()
            ax.grid(True)

        plt.tight_layout(rect=[0, 0.03, 1, 0.96])
        plt.show()

    print('Misclassified sample statistics:')
    print(common_misclassified_data.describe())
    print('Correctly classified abnormal statistics:')
    print(correctly_classified_abnormal_data.describe())

    mean_mis = common_misclassified_data.mean(axis=0)
    mean_corr = correctly_classified_abnormal_data.mean(axis=0)
    feature_diffs = (mean_mis - mean_corr).abs().sort_values(ascending=False)

    print('Top feature differences:')
    print(feature_diffs.head(20))

    plt.figure(figsize=(12, 8))
    sns.barplot(x=feature_diffs.head(20).values, y=feature_diffs.head(20).index, palette='coolwarm')
    plt.title('Top 20 Feature Differences')
    plt.xlabel('Absolute Difference')
    plt.ylabel('Feature')
    plt.grid(axis='x', linestyle='--')
    plt.show()

    return correctly_classified_abnormal_data


def perform_kmeans_on_misclassified(common_misclassified_data, common_misclassified_indices, k=2):
    print('Clustering commonly misclassified samples with K-Means...')

    if common_misclassified_data.empty:
        print('No data available for clustering.')
        return common_misclassified_data

    if len(common_misclassified_data) < k:
        k = len(common_misclassified_data)
        print(f'Reducing k to {k} because there are fewer samples than clusters.')

    if k == 0:
        return common_misclassified_data

    km = KMeans(n_clusters=k, random_state=config.RANDOM_STATE, n_init=10)
    clusters = km.fit_predict(common_misclassified_data.values)

    clustered = common_misclassified_data.copy()
    clustered['cluster'] = clusters

    colors = sns.color_palette('tab10', k)
    fig, axes = plt.subplots(len(common_misclassified_indices), 1, figsize=(12, len(common_misclassified_indices) * 3))
    if len(common_misclassified_indices) == 1:
        axes = [axes]

    for i, idx in enumerate(common_misclassified_indices):
        ax = axes[i]
        ax.plot(common_misclassified_data.loc[idx].values, color=colors[clusters[i]])
        ax.set_title(f'Sample {idx} - Cluster {clusters[i]}')
        ax.set_xlabel('Time Points')
        ax.set_ylabel('Scaled ECG Reading')
        ax.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    plt.show()

    if k > 1:
        mean_waveforms = [clustered[clustered['cluster'] == cid].drop(columns=['cluster']).mean(axis=0) for cid in sorted(clustered['cluster'].unique())]
        plt.figure(figsize=(12, 6))
        for cid, waveform in enumerate(mean_waveforms):
            plt.plot(waveform.values, label=f'Cluster {cid} Mean')
        plt.title('Cluster Mean Waveforms')
        plt.xlabel('Time Points')
        plt.ylabel('Scaled ECG Reading')
        plt.legend()
        plt.grid(True)
        plt.show()

    return clustered


def compare_misclassified_to_average_normal(common_misclassified_data, normal_data_autoencoder, common_misclassified_indices):
    print('Comparing misclassified samples to average normal waveform...')

    average_normal = normal_data_autoencoder.mean(axis=0)
    if common_misclassified_data.empty:
        print('No misclassified data available to compare.')
        return

    num_samples = min(5, len(common_misclassified_indices))
    fig, axes = plt.subplots(num_samples, 1, figsize=(12, num_samples * 3))
    if num_samples == 1:
        axes = [axes]

    fig.suptitle('Misclassified Samples vs. Average Normal ECG', fontsize=16)

    for i, idx in enumerate(common_misclassified_indices[:num_samples]):
        ax = axes[i]
        ax.plot(common_misclassified_data.loc[idx].values, label='Misclassified Sample', color='red')
        ax.plot(average_normal.values, label='Average Normal', color='green', linestyle='--')
        ax.set_title(f'Sample {idx}')
        ax.set_xlabel('Time Points')
        ax.set_ylabel('Scaled ECG Reading')
        ax.legend()
        ax.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    plt.show()
