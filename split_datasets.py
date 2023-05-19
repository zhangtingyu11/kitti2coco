import os
import random
import shutil

'''
将数据按照一定比例划分成训练集和验证集，目录结构：

data_dir
├── kitti
│   ├── image_2
│   │   ├── 000000.png
│   │   ├── 000001.png
│   │   ├── 000002.png
│   │   ├── 000003.png
│   │   ├── 000004.png
│   │   └── 000005.png
│   └── label_2
│       ├── 000000.txt
│       ├── 000001.txt
│       ├── 000002.txt
│       ├── 000003.txt
│       ├── 000004.txt
│       └── 000005.txt


最终得到的目录结构：
dest_dir
├── labels
│   ├── train_labels
│   │   ├── 000000.txt
│   │   ├── 000001.txt
│   │   ├── 000002.txt
│   │   ├── 000004.txt
│   │   └── 000005.txt
│   └── val_labels
│       └── 000003.txt
├── train
│   ├── 000000.png
│   ├── 000001.png
│   ├── 000002.png
│   ├── 000004.png
│   └── 000005.png
└── val
    └── 000003.png



'''
# 训练集占的比例
ratio = 0.9

# 设置随机种子以确保可重复性
random.seed(42)

# 指定数据集路径和训练/验证集路径
data_dir = "/home/zty/Dataset/Kitti_COCO/"
dest_dir = '/home/zty/Dataset/Kitti_COCO/'

train_img_dir = os.path.join(dest_dir, 'train2017')
train_label_dir = os.path.join(dest_dir, 'labels/train_labels')
val_img_dir = os.path.join(dest_dir, 'val2017')
val_label_dir = os.path.join(dest_dir, 'labels/val_labels')


# 创建训练/验证集文件夹
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# 获取该类别的所有图像
img_path = os.path.join(data_dir + 'image_2')
all_images = os.listdir(img_path)
num_images = len(all_images)

label_path = os.path.join(data_dir + 'label_2')

# 打乱顺序
random.shuffle(all_images)

# 计算分割点
# split_index = int(ratio * num_images)
train_images_file = "/home/zty/Dataset/Kitti_COCO/ImageSets/train.txt"
val_images_file = "/home/zty/Dataset/Kitti_COCO/ImageSets/val.txt"
with open(train_images_file, 'r') as f:
    train_images = f.readlines()
with open(val_images_file, 'r') as f:
    val_images = f.readlines()

for image_name in train_images:
    src_path = os.path.join(img_path, image_name.strip()+".png")
    dst_path = os.path.join(train_img_dir, image_name.strip()+".png")
    shutil.copyfile(src_path, dst_path)

    src_label_path = os.path.join(label_path, image_name.strip() + '.txt')
    dst_label_path = os.path.join(train_label_dir, image_name.strip() + '.txt')
    shutil.copyfile(src_label_path, dst_label_path)

# 将后10%的图像复制到验证集文件夹
for image_name in val_images:
    src_path = os.path.join(img_path, image_name.strip()+".png")
    dst_path = os.path.join(val_img_dir, image_name.strip()+".png")
    shutil.copyfile(src_path, dst_path)

    src_label_path = os.path.join(label_path, image_name.strip() + '.txt')
    dst_label_path = os.path.join(val_label_dir, image_name.strip() + '.txt')
    shutil.copyfile(src_label_path, dst_label_path)
    

print("数据集划分完成！" + "训练集图片数目: " + str(len(train_images)) + '验证集图片数目: '+ str(len(val_images)))
