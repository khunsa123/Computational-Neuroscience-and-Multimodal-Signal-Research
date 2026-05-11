import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_ecg_waveform(data, title, xlabel, ylabel, num_samples=3, fig_size=(15, 6), labels=None, line_colors=None):
    """Visualize example ECG waveforms from the dataset."""
    print(f'Plotting ECG waveforms: {title}')

    if 'label' in data.columns:
        unique_labels = sorted(data['label'].unique())
        label_names = {0: 'Normal', 1: 'Abnormal'}
        categories = unique_labels

        if labels is None:
            labels = [label_names.get(label, str(label)) for label in categories]
    else:
        categories = [None]
        labels = labels or ['ECG']

    if line_colors is None:
        line_colors = sns.color_palette('viridis', n_colors=len(categories))

    fig, axes = plt.subplots(len(categories), num_samples, figsize=fig_size)
    if len(categories) == 1 and num_samples == 1:
        axes = [[axes]]
    elif len(categories) == 1:
        axes = [axes]

    fig.suptitle(title, fontsize=16)

    for i, category in enumerate(categories):
        if category is None:
            category_data = data.copy()
        else:
            category_data = data[data['label'] == category].drop(columns=['label'])

        if category_data.empty:
            continue

        samples = category_data.sample(min(len(category_data), num_samples), random_state=42)

        for j, (_, row) in enumerate(samples.iterrows()):
            ax = axes[i][j]
            ax.plot(row.values, color=line_colors[i])
            ax.set_title(f'{labels[i]} Sample {j + 1}')
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    plt.show()


def plot_label_distribution(labels, title, xlabel, ylabel, fig_size=(7, 5)):
    """Plot the distribution of class labels."""
    print(f'Plotting label distribution for {xlabel}')

    label_counts = pd.Series(labels).value_counts().sort_index()
    print(label_counts)

    plt.figure(figsize=fig_size)
    sns.barplot(x=label_counts.index.astype(str), y=label_counts.values, palette='viridis')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', linestyle='--')
    plt.show()


def plot_confusion_matrix(cm, title, labels=['Normal', 'Abnormal'], fig_size=(8, 6)):
    """Plot a confusion matrix heatmap."""
    print(f'Plotting confusion matrix: {title}')

    plt.figure(figsize=fig_size)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.title(title)
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.show()
