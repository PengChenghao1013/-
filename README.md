# 基于VOC数据集的YOLO V3目标检测

## 简介

本项目使用MMDetection框架在VOC数据集上训练YOLO V3目标检测模型。为了兼容MMDetection，首先将VOC数据集转换为COCO格式。项目包括数据转换、模型训练和测试的脚本。

## 数据集

训练使用的数据库为VOC 2012。在训练之前，通过提供的脚本将VOC数据集转换为COCO格式。

## 先决条件

- Python 3.11
- requirements.txt文件中列出的其他依赖项

## 设置

1. 克隆仓库并进入项目目录
2. 安装所需的依赖项： pip install -r requirements.txt
3. 下载VOC 2012数据集并将其放置在VOCdevkit目录中

## 数据转换

使用提供的脚本将VOC数据集转换为COCO格式。

1. 移动图像： python move_img.py
2. 将VOC注释转换为COCO格式： python voc2coco.py

## 训练

使用提供的配置文件训练YOLO V3模型。从百度云（链接: https://pan.baidu.com/s/1dTs2CnOy1JDG9pneGAhgyA 提取码: wjry）下载预训练权重，并将其放置在checkpoints目录中。

1. 修改配置文件yolov3_d53_mstrain-608_273e_coco.py以指定数据集路径和其他设置。
2. 运行训练脚本： python yolov3_d53_mstrain-608_273e_coco.py

## 测试

使用提供的image_demo.py脚本测试训练好的模型。

1. 运行测试脚本： python image_demo.py

## 文件说明

- move_img.py：将图像移动到正确目录的脚本。
- voc2co.py：将VOC注释转换为COCO格式的脚本。
- yolov3_d53_mstrain-608_273e_coco.py：YOLO V3模型配置文件。
- image_demo.py：用于测试训练好模型的脚本。
- 20240513_100104文件夹：tensorboard可视化链接
