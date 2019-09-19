import datetime
starttime = datetime.datetime.now()
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import os
import glob
import cv2
from numpy import *

def Knn(kValue):
    X_train = []
    y_train = []
    path = 'D:/image/train/'
    path1 = 'D:/image/test/'
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

    # KNN分类算法函数定义
    def kNNClassify(newInput, dataSet, labels, k):
        numSamples = dataSet.shape[0]  # shape[0]表示行数
        # tile(A, reps): 构造一个矩阵，通过A重复reps次得到
        # the following copy numSamples rows for dataSet
        diff = np.tile(newInput, (numSamples, 1)) - dataSet  # 按元素求差值
        squaredDiff = diff ** 2  # 将差值平方
        squaredDist = sum(squaredDiff, axis=1)  # 按行累加
        distance = squaredDist ** 0.5  # 将差值平方和求开方，即得距离

        # # step 2: 对距离排序
        # argsort() 返回排序后的索引值
        sortedDistIndices = argsort(distance)
        classCount = {}  # define a dictionary (can be append element)
        for i in range(k):
            # # step 3: 选择k个最近邻
            voteLabel = labels[sortedDistIndices[i]]
            # # step 4: 计算k个最近邻中各类别出现的次数
            # when the key voteLabel is not in dictionary classCount, get()
            # will return 0
            classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

        # # step 5: 返回出现次数最多的类别标签
        maxCount = 0
        for key, value in classCount.items():
            if value > maxCount:
                maxCount = value
                maxIndex = key
        return maxIndex


    predictions = []
    for i in range(X_test.shape[0]):
        predictions_labes = kNNClassify(X_test[i], X_train, y_train, kValue)  # K值可以调，一般设的较小，5,10,15
        predictions.append(predictions_labes)
        ac = 0
        for i in range(len(predictions)):
            if y_test[i] == predictions[i]:
                ac += 1
    print(ac/len(y_test))
    # print(confusion_matrix(y_test, predictions))
    # # 打印预测结果混淆矩阵
    # print(classification_report(y_test, predictions))
    # 打印精度、召回率、FI结果
    endtime = datetime.datetime.now()
    print(endtime - starttime)
    return ac/len(y_test)
