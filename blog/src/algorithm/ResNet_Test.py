from torch.utils.data import DataLoader
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch import nn,optim
from torch.autograd import Variable
import torch
import time
from PIL import Image

# from Dataset import Handtest
from torchvision import transforms as T

if __name__ == '__main__':
    data_root = './Dataset/'
    save_root = './Save/'
    print("Loading dataset...")
    # train_data = Handtest(data_root)
    batch_size_train = 1
    num_workers = 1
    max_epoch = 1500
    # batch_size = batch_size if len(params.gpus) == 0 else batch_size*len(params.gpus)


    # train_dataloader = DataLoader(train_data, batch_size=batch_size_train, shuffle=False, num_workers=num_workers)
    # print('train dataset len: {}'.format(len(train_dataloader.dataset)))

    # val_dataloader = DataLoader(val_data, batch_size=batch_size_val, shuffle=False, num_workers=num_workers)
    # print('val dataset len: {}'.format(len(val_dataloader.dataset)))

    # 输出数据格式
    # for batch_datas,names in train_dataloader:
    #     print(batch_datas.size(),names)
    #     print(batch_datas.type(),names)
    #     break


    transforms_data = T.Compose([
        T.Scale(128),               #固定大小
        T.CenterCrop(128),
        T.ToTensor(),
        T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
    ])

    model = IrisNet = torch.load(save_root+'Epoch-10.pth')
    use_gpu = torch.cuda.is_available()
    #
    # if torch.cuda.device_count() > 1:
    #     print("Let's use", torch.cuda.device_count(), "GPUs!")
    #     model = nn.DataParallel(model, device_ids=[0]).cuda()
    #
    if torch.cuda.is_available():
        model.cuda()


    img = Image.open('C:\\Users\\44849\Desktop\\工程实训\\HandCode_Test\\Dataset\\testimg\\1.jpg')
    print(img.size)
    img = Variable(torch.unsqueeze(transforms_data(img), 0).cuda())
    out = model(img)
    #print(out)
    out = torch.max(out, 1)
    print(format(out[1]))

    # for i, data in enumerate(train_dataloader, 1):
    #     img, names = data
    #     if use_gpu:
    #         img = Variable(img.cuda())
    #     else:
    #         img = Variable(img)
    #     out = model(img)
    #     #print(out)
    #     out = torch.max(out, 1)
    #     #out = out.cup
    #
    #     print('%s Predicted Value:{}'%names,format(out[1]))




