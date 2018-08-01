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

import glob
import numpy as np

def load_training_data(path_to_train='../../data/raw/train/', image_width=128,
                       image_height=128, image_channels=1, sample_size=500):
    ''' This function is responsible for loading
    training images from the database. '''

    # Search the folder for png files.
    image_names = glob.glob(path_to_train+'images/*.png')
    n_images    = len(image_names)
    print('Found %d images.' % n_images)


    if sample_size is None:
        sample_size = n_images
    elif sample_size > n_images:
        sample_size = n_images

    print('Starting load of %d images' % sample_size)

    x_train = np.zeros((sample_size, image_height, image_width, image_channels), dtype=np.uint8)
    y_train = np.zeros((sample_size, image_height, image_width), dtype=np.bool)
    for index, image_name in enumerate(image_names[:sample_size]):
        image_id = image_name.split('.png')[0].split('/')[-1]

        # Load the data here.

# Main method used only for testing purposes.
if __name__ == '__main__':
    load_training_data('../../data/raw/train/', sample_size=10)    # Simple test
    load_training_data('../../data/raw/train/', sample_size=None)  # All loading test
    load_training_data('../../data/raw/train/', sample_size=10000) # All loading test