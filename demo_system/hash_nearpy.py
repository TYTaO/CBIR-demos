from nearpy import Engine
from nearpy.hashes import RandomBinaryProjections
import numpy
from nearpy.filters import NearestFilter

# Dimension of our vector space
dimension = 512

# Create a random binary hash with 10 bits
rbp = RandomBinaryProjections('rbp', 0)

# Create engine with pipeline configuration
engine = Engine(dimension, lshashes=[rbp], vector_filters=[NearestFilter(12)])
# 计算目标图片与数据库中每张图像的余弦相似度

def ann_nearpy(query, features): 
  for i in range(len(features)):
      engine.store_vector(features[i], i)
  return engine.neighbours(query)