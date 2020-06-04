## 需要前面的参数： 检索图片路径
## 返回： 结果的路径

from __future__ import print_function
from __future__ import division
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
print("PyTorch Version: ",torch.__version__)
print("Torchvision Version: ",torchvision.__version__)

import pickle as pk
from PIL import Image
import random

from pooling import RMAC
from utils import extract_features, save_data
from hash_nearpy import ann_nearpy

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 主函数
def retrieval(query_path):
  query = load_query_image(query_path)
  query = query.unsqueeze(dim=0)
  print(os.getcwd())
  net = load_model()
  query.to('cpu')
  net.to('cpu')
  net.eval()
  query_feature = net(query)
  query_feature = query_feature.view(512)
  features = load_features()

  ## 局部敏感哈希
  query_numpy = query_feature.detach().numpy()
  features_numpy = features.detach().numpy()
  res = ann_nearpy(query_numpy, features_numpy)

  # 得到结果序号
  sim = []
  for data in res:
      sim.append(data[1])

  # 
  Gallery_paths = get_Gallery_path()
  res_img_paths = []
  for i in sim:
    res_img_paths.append(Gallery_paths[i])
  return res_img_paths

# 加载特征
def load_features():
  save_path = './CBIR/features/rmac_L=2_UcRemote21-train-resnet'
  fo = open(save_path, 'rb')
  features = pk.load(fo, encoding='bytes')
  fo.close()
  print("Load features.")
  return features

# 加载模型
def load_model():
  pretrained_net = models.resnet34(pretrained=True)
  pretrained_net.avgpool = RMAC()
  pretrained_net.fc = nn.Sequential()
  PATH = "./CBIR/my_model/rmac_L=2_UcRemote_resnet34_fine-tune.pt"  # L其实=3
  pretrained_net.load_state_dict(torch.load(PATH))
  return pretrained_net

# 提取图片特征
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

# 得到数据库图片路径
def get_Gallery_path():
    file_dir = 'D:/360downloads/毕业论文/数据集/UCMerced_LandUse/data/test'
    x = os.listdir(file_dir)
    file_paths = []
    for file_dir_child in x :
        file_dir_child = file_dir+'/'+file_dir_child
        for file in os.listdir(file_dir_child):
            file_paths.append(file_dir_child + '/' + file)
    return file_paths

