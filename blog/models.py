from django.db import models

# 定义用户模型管理类
class UserManager(models.Manager):
    #创建模型类，接收参数为属性赋值
    def create_user(self, user_name, user_password):
        #创建模型类对象self.model可以获得模型类
        user = self.model()
        user.user_name = user_name
        user.user_password = user_password
        return user

# 定义用户模型管理类
class GETImages(models.Manager):
    #创建模型类，接收参数为属性赋值
    def create_user(self, user_name, user_password):
        #创建模型类对象self.model可以获得模型类
        user = self.model()
        user.user_name = user_name
        user.user_password = user_password
        return user

# 定义用户模型类
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=16)
    user_password = models.CharField(max_length=16)
    user_power = models.IntegerField(null=True,default=0)
    objects = UserManager()
    def __str__(self):
        return "%d" % self.pk

# 定义图片模型类（包含图像地址，图像用户标记，图像机器识别结果）
class Img(models.Model):
    img_id = models.AutoField(primary_key=True)
    img_url = models.CharField(max_length=128)
    img_sign = models.IntegerField(null=True,default=-1)
    img_result = models.IntegerField(null=True,default=-1)
    objects = models.Manager()
    def __str__(self):
        return "%d" % self.pk

