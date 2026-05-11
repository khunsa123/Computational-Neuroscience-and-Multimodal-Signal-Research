import config
import data_preprocessing
import autoencoder_model
import supervised_models
import misclassification_analysis
import model_evaluation


def main():
    print('Starting ECG Anomaly Detection and Classification workflow...')

    df_balanced, df_scaled = data_preprocessing.load_and_preprocess_data()
    if df_balanced is None or df_scaled is None:
        print('Data preprocessing failed. Exiting.')
        return

    X_train_normal, X_val_normal, X_normal_autoencoder, X_abnormal_autoencoder = autoencoder_model.prepare_autoencoder_data(df_balanced)
    autoencoder = autoencoder_model.build_autoencoder(config.AE_INPUT_DIM)
    autoencoder_model.train_autoencoder(autoencoder, X_train_normal, X_val_normal)
    mse_normal, mse_abnormal, ae_threshold = autoencoder_model.detect_anomalies(autoencoder, X_normal_autoencoder, X_abnormal_autoencoder)

    X_train, X_test, y_train, y_test, X_classifier = supervised_models.prepare_supervised_data(df_balanced)

    rf_classifier_initial, cm_rf_initial = supervised_models.train_evaluate_random_forest(X_train, X_test, y_train, y_test)
    supervised_models.plot_feature_importance(rf_classifier_initial, X_classifier.columns, 'RandomForest Feature Importance')

    best_rf_classifier, cm_tuned_rf = supervised_models.tune_random_forest(X_train, X_test, y_train, y_test)
    gbc_classifier, cm_gbc = supervised_models.train_evaluate_gradient_boosting(X_train, X_test, y_train, y_test)
    svm_classifier, cm_svm = supervised_models.train_evaluate_svm(X_train, X_test, y_train, y_test)

    model_evaluation.plot_roc_pr_curves_for_model(best_rf_classifier, X_test, y_test, title_prefix='Tuned RandomForestClassifier')
    model_evaluation.plot_roc_pr_curves_for_model(gbc_classifier, X_test, y_test, title_prefix='GradientBoostingClassifier')
    model_evaluation.plot_roc_pr_curves_for_model(svm_classifier, X_test, y_test, title_prefix='SVM Classifier')

    cms_dict = {
        'Tuned RandomForest': cm_tuned_rf,
        'GradientBoosting': cm_gbc,
        'SVM': cm_svm
    }
    model_evaluation.plot_comparative_confusion_matrices(cms_dict)

    normal_data_autoencoder_df = df_balanced[df_balanced['label'] == 0].drop(columns=['label'])
    abnormal_data_autoencoder_df = df_balanced[df_balanced['label'] == 1].drop(columns=['label'])

    y_pred_rf_initial = rf_classifier_initial.predict(X_test)
    misclassification_analysis.compare_autoencoder_vs_classifier_misclassifications(
        normal_data_autoencoder_df,
        abnormal_data_autoencoder_df,
        mse_normal,
        mse_abnormal,
        ae_threshold,
        X_test,
        y_test,
        y_pred_rf_initial,
        df_balanced
    )

    y_pred_tuned_rf = best_rf_classifier.predict(X_test)
    y_pred_gbc = gbc_classifier.predict(X_test)
    y_pred_svm = svm_classifier.predict(X_test)

    common_misclassified_data, common_misclassified_indices = misclassification_analysis.find_and_analyze_common_supervised_misclassifications(
        X_test,
        y_test,
        y_pred_tuned_rf,
        y_pred_gbc,
        y_pred_svm,
        best_rf_classifier,
        gbc_classifier,
        svm_classifier
    )

    misclassification_analysis.compare_common_misclassified_to_average_correct(
        common_misclassified_data,
        X_test,
        y_test,
        y_pred_tuned_rf
    )

    misclassification_analysis.perform_kmeans_on_misclassified(common_misclassified_data, common_misclassified_indices)
    misclassification_analysis.compare_misclassified_to_average_normal(
        common_misclassified_data,
        normal_data_autoencoder_df,
        common_misclassified_indices
    )

    print('ECG workflow complete.')


if __name__ == '__main__':
    main()
