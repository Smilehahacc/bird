from torch.autograd import Variable
import torch
from torchvision import transforms as T
import os

def result(img):
    save_root = os.getcwd()+ '/blog/src/algorithm/HandCode_Test/Save/'
    # save_root = os.getcwd() + '/HandCode_Test/Save/'  #运行测试代码时需要使用的地址（脱离django框架时）
    # 把图片transform为固定格式;
    transforms_data = T.Compose([
         T.Scale(128),  # 固定大小size=128
         T.CenterCrop(128),
         T.ToTensor(),
         T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    ])
    model = torch.load(save_root + 'Epoch-10.pth', map_location='cpu')  # 加载模型
    use_gpu = torch.cuda.is_available()
    if torch.cuda.is_available():
        model.cuda()
    # print(img.size)
    img = Variable(torch.unsqueeze(transforms_data(img), 0).cuda())
    out = model(img)
    out = torch.max(out, 1)
    return format(out[1])
