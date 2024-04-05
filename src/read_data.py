import scipy.io
import numpy as np

import os
import re

# Define the directory where you want to search
directory = 'data/physionet.org/files/ecg-arrhythmia/1.0.0/WFDBRecords'

# Define your regex pattern
pattern = re.compile(r'[0-9]{2}\/[0-9]{3}\/JS00001\.mat')  # For example, matches files ending with '.txt'

# Iterate through all files in the directory
for root, dirs, files in os.walk(directory):
    for file_name in files:
        # Check if the file name matches the regex pattern
        if pattern.match(file_name):
            # If it matches, construct the full file path
            file_path = os.path.join(root, file_name)
            # Now you can use file_path as needed
            print(file_path)  # Or do something else with the file_path

test_mat = scipy.io.loadmat("data/physionet.org/files/ecg-arrhythmia/1.0.0/WFDBRecords/01/010/JS00001.mat")
print(test_mat)
print(test_mat.keys())
print(test_mat['val'])

data = np.array(test_mat['val'])
print('shape', np.shape(data))