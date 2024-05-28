import cv2

root_path = 'I:/datasets/VOCdevkit/VOC2012/'         # voc路径
trainval_path = root_path + "ImageSets/Main/train.txt" # 改成 trainval.txt / test.txt
jpg_path = root_path + 'JPEGImages/'
save_path = "I:/datasets/VOCdevkit/train2017/"         # 改成 train2017 / val2017

with open(trainval_path,'r') as f:
    for ele in f.readlines():
        cur_jpgname = ele.strip()  # 提取当前图像的文件名
        total_jpgname = jpg_path + cur_jpgname + '.jpg' # 获取图像全部路径
        # 读取图像
        cur_img = cv2.imread(total_jpgname)
        # 保存图像
        cv2.imwrite(save_path + cur_jpgname + '.jpg',cur_img)
    print('Done!')
