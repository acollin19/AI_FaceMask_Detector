# Preprocessing, loading & analyzing the datasets

# Import PyTorch libraries
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib import image as mp_image
import seaborn as sns

# Required magic to display matplotlib plots in notebooks
# matplotlib inline

from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

# The images are in a folder named 'input/natural-images/natural_images'
# training_folder = '../images/Training'
# testing_folder = '../images/Testing'

img_folder = '../images'

# All images are 128x128 pixels
img_size = (128, 128)

# The folder contains a subfolder for each class of shape
# train_classes = sorted(os.listdir(training_folder))
# test_classes = sorted(os.listdir(testing_folder))

all_classes = sorted(os.listdir(img_folder))


def load_dataset(data_path):

    transformation = transforms.Compose([
        # Randomly augment the image data
        # Random horizontal flip
        transforms.RandomHorizontalFlip(0.5),
        # Random vertical flip
        transforms.RandomVerticalFlip(0.3),
        # transform to tensors
        transforms.ToTensor(),
        # Normalize the pixel values (in R, G, and B channels)
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    # Load & transform all of the images
    full_dataset = torchvision.datasets.ImageFolder(
        root=data_path,
        transform=transformation
    )

    # Split training/ testing (75% / 25%)
    train_size = int(0.75 * len(full_dataset))
    test_size = len(full_dataset) - train_size

    # use torch.utils.data.random_split for training/test split
    train_dataset, test_dataset = torch.utils.data.random_split(full_dataset, [train_size, test_size])

    # loader for training
    train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=20,
        num_workers=2,
        shuffle=True
    )

    # loader for testing
    test_loader = torch.utils.data.DataLoader(
        test_dataset,
        batch_size=20,
        num_workers=2,
        shuffle=False
    )

    return train_loader, test_loader


train_loader, test_loader = load_dataset(img_folder)

# train_loader = load_dataset('../images/Training')


# transformation = transforms.Compose([
#         # Randomly augment the image data
#         # # Random horizontal flip
#         # transforms.RandomHorizontalFlip(0.5),
#         # # Random vertical flip
#         # transforms.RandomVerticalFlip(0.3),
#         # transform to tensors
#         transforms.ToTensor(),
#         # Normalize the pixel values (in R, G, and B channels)
#         transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
#     ])
#
#
#
# #Load all of the images, transforming them
# train_dataset = torchvision.datasets.ImageFolder(
#     root='../images/Training',
#     transform=transformation
# )
#
# #define a loader for the training data we can iterate through in 50-image batches
# train_loader = torch.utils.data.DataLoader(
#     train_dataset,
#     batch_size=20,
#     num_workers=2,
#     shuffle=True
# )
#
#
# #Load all of the images, transforming them
# test_dataset = torchvision.datasets.ImageFolder(
#     root=testing_folder,
#     transform=transformation
# )
#
# #define a loader for the training data we can iterate through in 50-image batches
# test_loader = torch.utils.data.DataLoader(
#     test_dataset,
#     batch_size=20,
#     num_workers=2,
#     shuffle=False
# )
