import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score

import config


def plot_roc_pr_curves_for_model(classifier, X_test, y_test, title_prefix='Classifier'):
    """Plot ROC-AUC and Precision-Recall curves for the specified model."""
    print(f'Evaluating {title_prefix}...')

    y_pred_proba = classifier.predict_proba(X_test)[:, 1]

    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=config.FIGURE_SIZE_DEFAULT)
    plt.plot(fpr, tpr, color='darkorange', label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
    plt.title(f'{title_prefix} ROC Curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()

    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    avg_precision = average_precision_score(y_test, y_pred_proba)

    plt.figure(figsize=config.FIGURE_SIZE_DEFAULT)
    plt.plot(recall, precision, color='blue', label=f'PR curve (AP = {avg_precision:.2f})')
    plt.title(f'{title_prefix} Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend(loc='lower left')
    plt.grid(True)
    plt.show()

    print(f'{title_prefix} ROC-AUC: {roc_auc:.4f}, Average Precision: {avg_precision:.4f}')


def plot_comparative_confusion_matrices(cms_dict, labels=['Normal', 'Abnormal']):
    """Plot confusion matrices for multiple models side by side."""
    if not cms_dict:
        print('No confusion matrices to plot.')
        return

    num_models = len(cms_dict)
    fig, axes = plt.subplots(1, num_models, figsize=(num_models * config.FIGURE_SIZE_SMALL[0], config.FIGURE_SIZE_SMALL[1]))
    if num_models == 1:
        axes = [axes]

    fig.suptitle('Comparative Confusion Matrices', fontsize=16)

    for ax, (model_name, cm) in zip(axes, cms_dict.items()):
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels, ax=ax)
        ax.set_title(model_name)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
