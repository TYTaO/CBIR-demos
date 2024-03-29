# 遥感图像特征提取与检索示例

本项目针对遥感图像特征提取和检索任务，使用基于ImageNet数据集预训练的VGG16和ResNet34网络模型进行微调。我们尝试了多种特征聚合方法来提高性能。

为了优化特征存储、向量计算和特征检索效果，我们采用了PCA降维技术和扩展查询技术。此外，为了实现大规模遥感图像检索，我们使用了局部敏感哈希算法（LSH）。

本算法在UCMD数据集上进行了性能验证，以确保实现的方法具有较好的准确性和效率。

experiment目录包含了一系列实验及其结果。
demo_system目录提供了一个Web界面系统，用户可以通过上传图像并搜索相似的图像。
