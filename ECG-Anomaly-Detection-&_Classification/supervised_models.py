import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

import config
import utils


def prepare_supervised_data(df_balanced):
    """Split the balanced dataset into training and test sets for supervised classifiers."""
    print('Preparing supervised training and test data...')

    X = df_balanced.drop(columns=['label'])
    y = df_balanced['label']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.TEST_SIZE_SUPERVISED,
        random_state=config.RANDOM_STATE,
        stratify=y
    )

    print(f'X_train: {X_train.shape}, X_test: {X_test.shape}')
    return X_train, X_test, y_train, y_test, X


def train_evaluate_random_forest(X_train, X_test, y_train, y_test):
    """Train and evaluate a RandomForestClassifier."""
    print('Training RandomForestClassifier...')

    classifier = RandomForestClassifier(
        n_estimators=config.RF_N_ESTIMATORS,
        random_state=config.RANDOM_STATE,
        class_weight=config.RF_CLASS_WEIGHT
    )
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print('RandomForestClassifier performance:')
    print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    utils.plot_confusion_matrix(cm, 'RandomForestClassifier Confusion Matrix')
    return classifier, cm


def plot_feature_importance(classifier, feature_names, title, top_n=20):
    """Plot feature importances from a tree-based classifier."""
    print('Plotting feature importances...')

    importances = classifier.feature_importances_
    importance_series = pd.Series(importances, index=feature_names).sort_values(ascending=False)

    print('Top features:')
    print(importance_series.head(top_n))

    top_features = importance_series.head(top_n)
    plt.figure(figsize=config.FIGURE_SIZE_DEFAULT)
    sns.barplot(x=top_features.values, y=top_features.index, palette='viridis')
    plt.title(title)
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.grid(axis='x', linestyle='--')
    plt.show()


def tune_random_forest(X_train, X_test, y_train, y_test):
    """Tune RandomForest hyperparameters using GridSearchCV."""
    print('Tuning RandomForestClassifier...')

    rf = RandomForestClassifier(random_state=config.RANDOM_STATE)
    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=config.RF_HYPER_PARAM_GRID,
        cv=5,
        scoring='accuracy',
        n_jobs=-1,
        verbose=0
    )
    grid_search.fit(X_train, y_train)

    best_rf = grid_search.best_estimator_
    print(f'Best parameters: {grid_search.best_params_}')
    print(f'Best CV accuracy: {grid_search.best_score_:.4f}')

    y_pred = best_rf.predict(X_test)
    print('Tuned RandomForestClassifier performance:')
    print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    utils.plot_confusion_matrix(cm, 'Tuned RandomForestClassifier Confusion Matrix')
    return best_rf, cm


def train_evaluate_gradient_boosting(X_train, X_test, y_train, y_test):
    """Train and evaluate a GradientBoostingClassifier."""
    print('Training GradientBoostingClassifier...')

    classifier = GradientBoostingClassifier(
        n_estimators=config.GBC_N_ESTIMATORS,
        learning_rate=config.GBC_LEARNING_RATE,
        max_depth=config.GBC_MAX_DEPTH,
        random_state=config.RANDOM_STATE
    )
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print('GradientBoostingClassifier performance:')
    print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    utils.plot_confusion_matrix(cm, 'GradientBoostingClassifier Confusion Matrix')
    return classifier, cm


def train_evaluate_svm(X_train, X_test, y_train, y_test):
    """Train and evaluate an SVM classifier."""
    print('Training SVM classifier...')

    classifier = SVC(
        kernel=config.SVM_KERNEL,
        random_state=config.RANDOM_STATE,
        class_weight=config.SVM_CLASS_WEIGHT,
        probability=True
    )
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)
    print('SVM performance:')
    print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    utils.plot_confusion_matrix(cm, 'SVM Confusion Matrix')
    return classifier, cm
