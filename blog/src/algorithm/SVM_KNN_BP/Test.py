from blog.src.algorithm.SVM_KNN_BP.KNN import Knn
from blog.src.algorithm.SVM_KNN_BP.bp import Bp
from blog.src.algorithm.SVM_KNN_BP.hog_svm import Svm


def get_knn(kValue):
  return Knn(kValue)

def get_bp(learningRate,epochs):
  return Bp(learningRate,epochs)

def get_svm():
  return Svm()
