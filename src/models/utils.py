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

from skimage.io import imread

def load_data(path='../../data/raw/', image_width=128,
                       image_height=128, image_channels=1, sample_size=None):
    ''' This function is responsible for loading
    training images from the database. '''

    # The depth of all testing and training images.
    depths = pd.read_csv(path + 'depths.csv', nrows=sample_size)
    train = pd.read_csv(path + 'train.csv', nrows=sample_size)

    # Use depth information to find training and testing IDs
    train_ids = train['id'].values
    test_ids = [id for id in depths['id'].values if id not in train_ids]

    train_images = [imread('{}train/images/{}.png'.format(path, id)) for id in train_ids]
    train_masks = [imread('{}train/masks/{}.png'.format(path, id)) for id in train_ids]

    test_images = [imread('{}test/images/{}.png'.format(path, id)) for id in test_ids]
    test_masks = [imread('{}test/masks/{}.png'.format(path, id)) for id in test_ids]

    train_df = pd.DataFrame({
        'id':train_ids,
        'image':train_images,
        'mask':train_masks
    })

    test_df = pd.DataFrame({
        'id':test_ids,
        'image':test_images,
        'mask':test_masks
    })

    return train_df, test_df

# Main method used only for testing purposes.
if __name__ == '__main__':
    load_data('../../data/raw/', sample_size=10)    # Simple test
    load_data('../../data/raw/', sample_size=None)  # All loading test
    load_data('../../data/raw/', sample_size=10000) # All loading test