import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

import config


def prepare_autoencoder_data(df_balanced):
    """Prepare data for autoencoder training and evaluation."""
    print('Preparing autoencoder data...')

    normal_data = df_balanced[df_balanced['label'] == 0].drop(columns=['label'])
    abnormal_data = df_balanced[df_balanced['label'] == 1].drop(columns=['label'])

    X_normal_autoencoder = normal_data.values
    X_abnormal_autoencoder = abnormal_data.values

    from sklearn.model_selection import train_test_split
    X_train_normal, X_val_normal = train_test_split(
        X_normal_autoencoder,
        test_size=config.TEST_SIZE_SUPERVISED,
        random_state=config.RANDOM_STATE
    )

    print(f'Normal training shape: {X_train_normal.shape}')
    print(f'Normal validation shape: {X_val_normal.shape}')
    print(f'Abnormal evaluation shape: {X_abnormal_autoencoder.shape}')

    return X_train_normal, X_val_normal, X_normal_autoencoder, X_abnormal_autoencoder


def build_autoencoder(input_dim):
    """Build and compile the autoencoder model."""
    print('Building autoencoder model...')

    input_layer = Input(shape=(input_dim,))
    encoder = Dense(64, activation='relu')(input_layer)
    encoder = Dense(32, activation='relu')(encoder)
    latent_space = Dense(config.AE_LATENT_DIM, activation='relu')(encoder)

    decoder = Dense(32, activation='relu')(latent_space)
    decoder = Dense(64, activation='relu')(decoder)
    output_layer = Dense(input_dim, activation='linear')(decoder)

    autoencoder = Model(inputs=input_layer, outputs=output_layer)
    autoencoder.compile(optimizer='adam', loss='mse')

    print('Autoencoder compiled.')
    autoencoder.summary()
    return autoencoder


def train_autoencoder(autoencoder, X_train_normal, X_val_normal):
    """Train the autoencoder on normal ECG samples."""
    print('Training autoencoder...')

    history = autoencoder.fit(
        X_train_normal,
        X_train_normal,
        epochs=config.AE_EPOCHS,
        batch_size=config.AE_BATCH_SIZE,
        validation_data=(X_val_normal, X_val_normal),
        shuffle=True,
        verbose=0
    )

    print('Autoencoder training complete.')
    plt.figure(figsize=config.FIGURE_SIZE_DEFAULT)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Autoencoder Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss (MSE)')
    plt.legend()
    plt.grid(True)
    plt.show()

    return history


def detect_anomalies(autoencoder, X_normal_autoencoder, X_abnormal_autoencoder):
    """Detect anomalies using reconstruction error from the autoencoder."""
    print('Detecting anomalies...')

    reconstructions_normal = autoencoder.predict(X_normal_autoencoder, verbose=0)
    mse_normal = np.mean(np.power(X_normal_autoencoder - reconstructions_normal, 2), axis=1)

    reconstructions_abnormal = autoencoder.predict(X_abnormal_autoencoder, verbose=0)
    mse_abnormal = np.mean(np.power(X_abnormal_autoencoder - reconstructions_abnormal, 2), axis=1)

    plt.figure(figsize=config.FIGURE_SIZE_DEFAULT)
    sns.histplot(mse_normal, bins=50, kde=True, color='blue', label='Normal', stat='density')
    sns.histplot(mse_abnormal, bins=50, kde=True, color='red', label='Abnormal', stat='density')
    plt.title('Reconstruction Error Distribution')
    plt.xlabel('MSE')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.show()

    threshold = np.percentile(mse_normal, config.AE_ANOMALY_THRESHOLD_PERCENTILE)
    print(f'Anomaly threshold set at the {config.AE_ANOMALY_THRESHOLD_PERCENTILE}th percentile: {threshold:.6f}')

    predicted_labels_normal = (mse_normal > threshold).astype(int)
    predicted_labels_abnormal = (mse_abnormal > threshold).astype(int)

    print(f'Normal samples flagged anomalous: {np.sum(predicted_labels_normal)} / {len(mse_normal)}')
    print(f'Abnormal samples flagged anomalous: {np.sum(predicted_labels_abnormal)} / {len(mse_abnormal)}')

    return mse_normal, mse_abnormal, threshold
