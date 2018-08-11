#!/usr/bin/env python
#
# utils.py
# Author: David Riser
# Date: August 1, 2018
#
# Utility functions used in src/model/
# codes are stored in this python file.
# Many of them are taken from Kaggle
# kernels, in the spirit of re-use.
# If the function is theirs, I have
# given citation below.

import numpy as np
import pandas as pd

from keras.preprocessing.image import load_img

def load_data(path='../../data/raw/', image_width=128,
                       image_height=128, image_channels=1, sample_size=None):
    ''' This function is responsible for loading
    training images from the database. '''

    train_ids, test_ids = find_indices()
    depths = load_depths()

    train_df = construct_training_df(train_ids, depths)
    test_df = construct_testing_df(test_ids, depths)

    train_df['image'] = load_train_images()
    train_df['mask'] = load_train_masks()
    test_df['image'] = load_test_images()
    test_df['mask'] = load_test_masks()

    return train_df, test_df

# Main method used only for testing purposes.
if __name__ == '__main__':
    load_data('../../data/raw/', sample_size=10)    # Simple test
    load_data('../../data/raw/', sample_size=None)  # All loading test
    load_data('../../data/raw/', sample_size=10000) # All loading test