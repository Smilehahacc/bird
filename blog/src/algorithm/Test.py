from PIL import Image
from blog.src.algorithm.CLASS import result
import os
local_url = os.getcwd()+ '/bird-vue/src/assets/test/'

# img = Image.open(local_url +'/bird/bird-vue/src/assets/test/1.jpg')  # 测试图片位置
# print(result(img))

def start_sort(url):
    img = Image.open(local_url+url)  # 测试图片位置
    return result(img)
