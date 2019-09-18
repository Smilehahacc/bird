import datetime

starttime = datetime.datetime.now()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import os
import glob
import cv2

def Knn(kValue):
    X_train = []
    y_train = []
    path='D:/image/train/'
    path1='D:/image/test/'
    cate = [path + x for x in os.listdir(path) if os.path.isdir(path + x)]
    cate1 = [path1 + x for x in os.listdir(path1) if os.path.isdir(path1 + x)]
    for idx, folder in enumerate(cate):
        for im in glob.glob(folder + '/*.jpg'):
            # 打开一张图片并灰度化
            Images = cv2.imread(im)
            image = cv2.resize(Images, (256, 256), interpolation=cv2.INTER_CUBIC)
            hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
            X_train.append((hist / 255).flatten())
            y_train.append(idx)
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = []
    y_test = []
    for idx, folder in enumerate(cate1):
        for im in glob.glob(folder + '/*.jpg'):
            # 打开一张图片并灰度化
            Images = cv2.imread(im)
            image = cv2.resize(Images, (256, 256), interpolation=cv2.INTER_CUBIC)
            hist = cv2.calcHist([image], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
            X_test.append((hist / 255).flatten())
            y_test.append(idx)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    # 随机率为100%（保证唯一性）选取其中的30%作为测试集

    class KNN:
        def __init__(self, train_data, train_label, test_data):
            self.train_data = train_data
            self.train_label = train_label
            self.test_data = test_data

        def knnclassify(self):
            num_train = (self.train_data).shape[0]
            num_test = (self.test_data).shape[0]
            labels = []
            for i in range(num_test):
                y = []
                for j in range(num_train):
                    dis = np.sum(np.square((self.train_data)[j] - (self.test_data)[i]))
                    y.append(dis)
                labels.append(self.train_label[y.index(min(y))])
            labels = np.array(labels)
            return labels


    knn = KNN(X_train, y_train, X_test)
    predictions_labels = knn.knnclassify()
    ac = 0
    for i in range(len(y_test)):
        if y_test[i] == predictions_labels[i]:
            ac += 1
    print(ac/len(y_test))
    # print(confusion_matrix(y_test, predictions_labels))
    # print(classification_report(y_test, predictions_labels))
    endtime = datetime.datetime.now()
    print(endtime - starttime)
    return ac/len(y_test)
