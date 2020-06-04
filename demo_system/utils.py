# -*- coding: utf-8 -*-
from torchvision.datasets import ImageFolder
from PIL import Image
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from torchvision import transforms
import pooling

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
from torch.nn import functional as F

import pickle as pk
from PIL import Image
import random


# test
def say_ok():
    print('YES OK')

def save_data(file, data):
    f = open(file, 'wb+')
    pk.dump(data, f, 0)
    f.close()


def extract_features(model, loader):
    since = time.time()
    features = torch.FloatTensor()
         
    model.eval()

    # Iterate over data.
    for inputs, labels in loader:

        inputs = inputs.to(device)
        labels = labels.to(device)

        outputs = model(inputs)
        ff = outputs.data.cpu()
        # norm feature
        fnorm = torch.norm(ff, p=2, dim=1, keepdim=True)
        ff = ff.div(fnorm.expand_as(ff))
        features = torch.cat((features, ff), 0)

    time_elapsed = time.time() - since
    print('Feature extraction complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    
    return features


def load_net(PATH):
    pretrained_net = models.resnet34(pretrained=True)
    pretrained_net.avgpool = pooling.RMAC() # pooling
    pretrained_net.fc = nn.Sequential()
    pretrained_net.load_state_dict(torch.load(PATH))
    return pretrained_net

def load_query_image(query_path):
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    # mean = [0.485, 0.456, 0.406]  std = [0.229, 0.224, 0.225]
    test_augs = transforms.Compose([
        transforms.Resize(size=256),
        transforms.CenterCrop(size=224),
        transforms.ToTensor(),
        normalize
    ])
    query_image = datasets.folder.default_loader(query_path)
    query_image = test_augs(query_image)
    return query_image

def get_img_path(file_dir):
    x = os.listdir(file_dir)
    file_paths = []
    for file_dir_child in x :
        file_dir_child = file_dir+'/'+file_dir_child
        for file in os.listdir(file_dir_child):
            file_paths.append(file_dir_child + '/' + file)
    return file_paths
