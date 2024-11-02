import sys
import os
import numpy as np
import librosa
import pandas as pd
import sklearn

from feature_engineering import *
from config import CreateDataset

data_path = CreateDataset.data_path
csv_name = CreateDataset.Name

# file load
def get_sampels(data_set='train'):
    audios = []
    labels = []
    path_of_audios = librosa.util.find_files(data_path + data_set, ext=['mp3'])
    for audio in path_of_audios:
        # Extract instrument name from path
        instrument = audio.split('/')[-2]
        labels.append(instrument)
        try:
            y, sr = librosa.load(audio, sr=22050, duration=4.0, mono=True)
            if len(y) < sr * 4:  # Ensure 4 seconds of audio
                y = np.pad(y, (0, sr * 4 - len(y)))
            audios.append(y)
        except Exception as e:
            print(f"Error loading {audio}: {str(e)}")
            continue
    audios_numpy = np.array(audios)
    return audios_numpy, labels

def main():
    is_created = False
    audios_numpy, labels = get_sampels(data_set='train')
    for samples in audios_numpy:
        row = extract_feature(samples)
        if not is_created:
            dataset_numpy = np.array(row)
            is_created = True
        elif is_created:
            dataset_numpy = np.vstack((dataset_numpy, row))

    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1,1))
    dataset_numpy = scaler.fit_transform(dataset_numpy)

    dataset_pandas = pd.DataFrame(dataset_numpy)
    dataset_pandas["instruments"] = labels
    dataset_pandas.to_csv(csv_name, index=False)

if __name__ == '__main__':
    main()
