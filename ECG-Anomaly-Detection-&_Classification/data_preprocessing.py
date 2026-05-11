import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

import config
from download_data import ensure_dataset_downloaded


def load_and_preprocess_data():
    """Load the ECG dataset, preprocess features, and balance classes with SMOTE."""
    print('Starting data loading and preprocessing...')

    if not ensure_dataset_downloaded():
        return None, None

    try:
        df = pd.read_csv(config.DATA_PATH)
        print(f"Dataset loaded successfully from {config.DATA_PATH}.")
    except Exception as exc:
        print(f"An error occurred while loading the dataset: {exc}")
        return None, None

    if '1.0' in df.columns:
        df = df.rename(columns={'1.0': 'label'})
        print("Column '1.0' renamed to 'label'.")

    if 'label' not in df.columns:
        last_column = df.columns[-1]
        df = df.rename(columns={last_column: 'label'})
        print(f"Assumed label column and renamed '{last_column}' to 'label'.")

    if 'label' in df.columns:
        df['label'] = df['label'].astype(int)
        print("Column 'label' converted to integer type.")
    else:
        print("Error: Could not find or infer a label column.")
        return None, None

    total_missing_values = df.isnull().sum().sum()
    if total_missing_values == 0:
        print('No missing values found in the dataset.')
    else:
        print(f'Total missing values detected: {total_missing_values}. Filling with column means.')
        df = df.fillna(df.mean())

    X = df.drop(columns=['label'])
    y = df['label']
    print('Separated features and target label.')

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
    print('Applied StandardScaler to features.')

    df_scaled = pd.concat([X_scaled_df, y.reset_index(drop=True)], axis=1)
    print('Created scaled dataset for autoencoder training.')

    print('Original label distribution:')
    print(y.value_counts())

    smote = SMOTE(random_state=config.SMOTE_RANDOM_STATE)
    X_resampled, y_resampled = smote.fit_resample(X_scaled_df, y)
    df_balanced = pd.concat([
        pd.DataFrame(X_resampled, columns=X.columns),
        pd.Series(y_resampled, name='label')
    ], axis=1)

    print('Applied SMOTE to balance the dataset.')
    print('Balanced label distribution:')
    print(df_balanced['label'].value_counts())

    return df_balanced, df_scaled
