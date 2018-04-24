from ctypes import c_bool

import numpy as np
import re
import itertools
from collections import Counter


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(data_file_1, data_file_2, data_file_3, data_file_4, data_file_5):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    data_1 = list(open(data_file_1, "r", encoding='UTF8').readlines())
    data_1 = [s.strip() for s in data_1]
    data_2 = list(open(data_file_2, "r", encoding='UTF8').readlines())
    data_2 = [s.strip() for s in data_2]
    data_3 = list(open(data_file_3, "r", encoding='UTF8').readlines())
    data_3 = [s.strip() for s in data_3]
    data_4 = list(open(data_file_4, "r", encoding='UTF8').readlines())
    data_4 = [s.strip() for s in data_4]
    data_5 = list(open(data_file_5, "r", encoding='UTF8').readlines())
    data_5 = [s.strip() for s in data_5]

    # Split by words
    x_text = data_1 + data_2 + data_3 + data_4 + data_5
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    data_labels_1 = [[1, 0, 0, 0, 0] for _ in data_1]
    data_labels_2 = [[0, 1, 0, 0, 0] for _ in data_1]
    data_labels_3 = [[0, 0, 1, 0, 0] for _ in data_1]
    data_labels_4 = [[0, 0, 0, 1, 0] for _ in data_1]
    data_labels_5 = [[0, 0, 0, 0, 1] for _ in data_1]
    y = np.concatenate([data_labels_1, data_labels_2, data_labels_3, data_labels_4, data_labels_5], 0)
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]