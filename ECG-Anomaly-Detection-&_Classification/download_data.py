import os
import zipfile

import config


def ensure_dataset_downloaded():
    """Download the ECG dataset from Kaggle if it is not already present."""
    if os.path.exists(config.DATA_PATH):
        print(f'Dataset already exists at {config.DATA_PATH}.')
        return True

    os.makedirs(os.path.dirname(config.DATA_PATH), exist_ok=True)

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError:
        print('The Kaggle API package is not installed. Install with `pip install kaggle`.')
        return False

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as exc:
        print('Kaggle authentication failed. Configure your Kaggle credentials in ~/.kaggle/kaggle.json or set KAGGLE_USERNAME and KAGGLE_KEY.')
        print(exc)
        return False

    print(f'Downloading dataset from Kaggle: {config.KAGGLE_DATASET} ...')
    try:
        downloaded_path = api.dataset_download_file(
            config.KAGGLE_DATASET,
            config.KAGGLE_FILE,
            path=os.path.dirname(config.DATA_PATH),
            force=False,
            quiet=False
        )
    except Exception as exc:
        print(f'Dataset download failed: {exc}')
        return False

    if downloaded_path.endswith('.zip'):
        with zipfile.ZipFile(downloaded_path, 'r') as archive:
            archive.extract(config.KAGGLE_FILE, path=os.path.dirname(config.DATA_PATH))
        os.remove(downloaded_path)

    if not os.path.exists(config.DATA_PATH):
        print(f'Failed to locate downloaded file at {config.DATA_PATH}.')
        return False

    print(f'Download complete: {config.DATA_PATH}')
    return True


if __name__ == '__main__':
    success = ensure_dataset_downloaded()
    if success:
        print('Dataset download finished successfully.')
    else:
        print('Dataset download failed.')
