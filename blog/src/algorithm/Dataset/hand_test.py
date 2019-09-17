# -*- coding:utf-8 -*-
import os
from PIL import Image
from torch.utils import data
from torchvision import transforms as T
import torch as t
from torch.autograd import Variable
import numpy as np


class Handtest(data.Dataset):

    def __init__(self, root,transforms=None):
        '''
        Get images, divide into train/val set
        '''
        self.images_root = root
        self.size = 128
        if transforms is None:
            self.transforms_data = T.Compose([
                T.Scale(self.size),
                T.CenterCrop(self.size),
                T.ToTensor(),
                T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
            ])

        self._read_txt_file()

    def _read_txt_file(self):
        self.images_path = []
        self.images_labels = []

        img_path = os.listdir(self.images_root+'testimg/')  # 读取图片地址，listdir读取文件夹下所有图片，修改为读取单张图片

        for img in img_path:
            self.images_path.append(img)

    def __getitem__(self, index):
        '''
        return the data of one image
        '''
        data_path = self.images_root  + 'testimg/' + self.images_path[index]

        data = Image.open(data_path)
        data = data.convert('RGB')
        Data = self.transforms_data(data)


        # *Img.getcolors()
        # Label = self.transforms_label(label)

        return Data,str(self.images_path[index])

    def __len__(self):
        return len(self.images_path)


    # 1. 用PIL读取图片
    #     # 2. 使用pytorch的transforms读取PIL的Image
    #     # 3. 使用ToTensor转换
    #     # 4. 送入model