import shutil
import json
import os

testing_data_list = []
with open('D:/TenGrad/Tiny ImageNet 200/IMagenet/tiny-imagenet-200/val/val_annotations.txt', 'r') as f:
  for line in f.readlines():
    file, label = line.split()[0:2]
    file_dir = 'D:/TenGrad/Tiny ImageNet 200/IMagenet/tiny-imagenet-200/val/images/' + file
    folder_path = 'D:/TenGrad/Tiny ImageNet 200/IMagenet/tiny-imagenet-200/val/' + label
    try: 
        os.mkdir(folder_path)
        shutil.copy(file_dir, folder_path)

    except:
        shutil.copy(file_dir, folder_path)