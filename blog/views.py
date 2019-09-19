from django.http import HttpResponse
from django.http import JsonResponse
from urllib.request import urlretrieve
from .models import User, Img
import json
import os
import random
import re
import requests
import urllib
from .src.util import zhenzismsclient as smsclient
from blog.src.algorithm.HandCode_Test.Test import start_sort
from blog.src.algorithm.SVM_KNN_BP.Test import get_knn
from blog.src.algorithm.SVM_KNN_BP.Test import get_bp
from blog.src.algorithm.SVM_KNN_BP.Test import get_svm

'''
**********登录页面的请求**********
'''
def login(request):
    if request.method == "GET":
        username = request.GET.get('username')
        password = request.GET.get('password')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    # 确保用户名和密码都不为空
    if username and password:
        # username = username.strip()
        try:
            user = User.objects.get(user_name=username)
        except:
            print('请求失败，未查询到用户！')
            return HttpResponse('ERROR')
        if user.user_password == password.strip():
            return HttpResponse('SUCCESS')
    print('密码错误！')
    return HttpResponse('ERROR')

# 通过用户名查找用户（用户登录后的用户信息获取）
def findUser(request):
    if request.method == "GET":
        username = request.GET.get('username')
    if request.method == "POST":
        username = request.POST.get('username')
    try:
        user = User.objects.filter(user_name=username)
        data = {}
        data["User"] = list(user.values())
        return JsonResponse(data,safe=False)
    except:
        print('请求失败，未查询到用户！')
        return HttpResponse("")

# 发送短信验证码
def sendSms(request):
    if request.method == "GET":
        phone = request.GET.get('phone')
    if request.method == "POST":
        phone = request.POST.get('phone')
    # 设置验证码有效时间
    # 确保手机号未被注册
    if phone_check(phone):
        code = sms_send(phone)
        # response =HttpResponse('ok')
        # response.set_cookie(phone, code, 60 * min)
        # request.session[phone] = code
        return HttpResponse(code)
    return HttpResponse("ERROR")

#号码检查
def phone_check(phone):
    try:
        User.objects.get(user_name=phone)
        return False
    except:
        return True


#调用接口，发送验证码
def sms_send(phone):
    code = code_get(6,False)
    client = smsclient.ZhenziSmsClient("https://sms_developer.zhenzikj.com","101456", "d09395be-b8f0-4285-9bb4-1c41c1d5fe23")
    result = client.send(phone, "您的验证码为:"+code+"，5分钟内输入有效，立即注册")
    print("发送的结果为："+result+"验证码为："+code)
    return code

# 随机数生成验证码
def code_get(n,alpha):
    s = '' # 创建字符串变量,存储生成的验证码
    for i in range(n):  # 通过for循环控制验证码位数
        num = random.randint(0,9)  # 生成随机数字0-9
        if alpha: # 需要字母验证码,不用传参,如果不需要字母的,关键字alpha=False
            upper_alpha = chr(random.randint(65,90))
            lower_alpha = chr(random.randint(97,122))
            num = random.choice([num,upper_alpha,lower_alpha])
        s = s + str(num)
    return s

# 通过手机号注册
def register(request):
    if request.method == "GET":
        phone = request.GET.get('phone')
        # code = request.GET.get('code')
        # session_code = request.session.get(phone,'sb')
        # print("now cookie is "+session_code)
        # if session_code != code:
        #     return HttpResponse("ERROR")
    if phone_check(phone):
        # 注册完毕，默认密码与手机号相同
        user=User.objects.create_user(phone,phone)
        user.save()
        return HttpResponse("SUCCESS")
    return HttpResponse("ERROR")


'''
**********爬虫页面的请求**********
'''
def getsearch(request):
    data = request.GET.get('inputdata')
    time = request.GET.get('timevalue') # 获取不到时间值
    source = request.GET.get('source')
    print(data)
    print(time)
    print(source)
    word = data
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    if source == '百度':
        dowmloadPic(result.text, word)
    if source == '搜狗':
        getSogoulmag(data,60,'../bird/blog/images/')
    if source == '360':
        key_q = data
        ps = 81
        sn = 88
        for i in range(0,1):  # 爬取多少图片 1页60张
            key_ps = ps+i*60
            key_sn = sn+i*60
            image_spider(key_q, key_ps, key_sn)
    if data:
        return HttpResponse('SUCCESS')
    HttpResponse('ERROR')

def dowmloadPic(html, keyword):
    # 百度图片爬虫
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        # dir = keyword + '_' + str(i) + '.jpg'
        dir =  '../bird/blog/images/' + keyword + '_' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        data = open(r"../bird/blog/address.txt","a+")
        txt = str(i) + '  ' +str(each)
        data.write(txt)
        data.write('\r\n')
        data.close()
        i += 1

def getSogoulmag(category,length,path):
    # 搜狗爬虫
    n=length
    cate=category
    # 获取的是图片所有信息
    imgs=requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+
                      '&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))

    # 转换成为json格式
    jd=json.loads(imgs.text)
    # all_items所有的图片
    jd=jd['all_items']

    imgs_t=[]
    for j in jd:
        # 通过定位bthumbUrl获取图片
        imgs_t.append(j['bthumbUrl'])
    m=1
    for img in imgs_t:
        # 打印某一张图片正在下载
        # print(str(m)+'.jpg'+'Downlod......')
        print(img)
        data = open(r"../bird/blog/address.txt","a+")
        txt = str(m) + '  ' + str(img)
        data.write(txt)
        data.write('\r\n')
        data.close()
        # 用来把远程数据下载到本地
        urllib.request.urlretrieve(img,path+cate+'_'+str(m)+'.jpg')
        m=m+1
    print('Complete!')

def image_spider(key_q, key_ps, key_sn):  
    # 360爬虫
    url = "http://image.so.com/j?q=nba&src=srp&correct=nba&pn=60&ch=&sn=208&ps=201&pc=60&pd=1&prevsn=148" \
          "&sid=39b8dabeae51031efce5a8d8b1fc6957&ran=0&ras=6&cn=0&gn=0&kn=8&comm=1"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        'Referer': "http://image.so.com/i?q=nba&src=srp"
    }
    params = {
        'q': key_q,
        'src': 'srp',
        'pn': '60',
        'ch': '',
        'sn': key_sn,
        'ps': key_ps,
        'pc': '60',
        'pd': '1',
        'prevsn': '0',
        'sid': 'd34ad660320d853f00ea2d476ba2eaa5',
        'ran': '0',
        'ras': '6',
        'cn': '0',
        'gn': '0',
        'kn': '8',
        'comm': '1'
    }

    response = requests.get(url, headers=headers, params=params).json()  # 转json
    lists = response.get('list')  # 提取list件，值为一个列表
    i = 1

    for lis in lists:
        # 遍历列表，提取其中img字符串（图片url)
        txt = str(key_q) + '_' + str(i)
        path = '../bird/blog/images/%s.jpg' % str(txt)  # 图片地址
        urlretrieve(lis.get('img'), path)  # 保存图片
        data = open(r"../bird/blog/address.txt","a+")
        num = str(i) + '  ' + str(lis.get('img'))
        data.write(num)
        data.write('\r\n')
        data.close()
        print(txt,lis.get('img'))
        i+=1

'''
**********图像标记页面的请求**********
'''
def getsign(request):
    try:
        img_list=[]
        for i in Img.objects.filter(img_sign = -1):
            dict = {'id':i.img_id,'url':i.img_url,'sort':i.img_sign}
            img_list.append(dict)
    except:
        print('请求失败！')
        return HttpResponse('ERROR')
    if img_list:
        data = {}
        data["images"] = list(img_list)
        return JsonResponse(data,safe=False)
    print('获取图片失败！')
    return HttpResponse('ERROR')


def pushsign(request):
    if request.method == "GET":
        uploadList = request.GET.get('images')
        imgList = json.loads(uploadList)
    try:
        for i in range(len(imgList)):
            index = imgList[i]['id']
            sort = imgList[i]['sort']
            Img.objects.filter(img_id=index).update(img_sign=sort)
    except:
        print('请求失败！')
        return HttpResponse('ERROR')
    return HttpResponse('SUCCESS')

'''
**********图像分类页面的请求**********
'''
# 将前端接收的图片地址输入分类算法中
def imgSort(request):
    if request.method == "GET":
        uploadList = request.GET.get('uploadList')
    imgList = json.loads(uploadList)
    try:
        for i in range(len(imgList)):
            print("正在识别第" + str(i + 1) + "张图像(" + imgList[i]['url'] + ")...")
            imgList[i]['sort'] = getResult(start_sort(imgList[i]['url']))
        print("全部识别完毕！")
        return HttpResponse(json.dumps(imgList), content_type='application/json')
    except Exception as e:
        print("图像识别失败！错误信息为："+str(e))
        return HttpResponse("ERROR")


# 提取分类算法回传结果
def getResult(result):
    if(result[8:9]=='0'):
        return "非鸟类"
    else:
        return "鸟类"
'''
**********算法评估页面的请求**********
'''
def getKnn(request):
    if request.method == "GET":
        kValue = request.GET.get('kValue')
    try:
        print("正在计算KNN算法准确率...")
        rate = "%.2f%%" % (get_knn(int(kValue)) * 100)
        return HttpResponse(rate)
    except Exception as e:
        print("KNN算法准确率计算失败！错误信息为："+str(e))
        return HttpResponse("ERROR")

def getBp(request):
    if request.method == "GET":
        learningRate = request.GET.get('learningRate')
        epochs = request.GET.get('epochs')
    try:
        print("正在计算BP算法准确率...")
        rate = "%.2f%%" % (get_bp(float(learningRate),int(epochs)) * 100)
        return HttpResponse(rate)
    except Exception as e:
        print("BP算法准确率计算失败！错误信息为："+str(e))
        return HttpResponse("ERROR")

def getSvm(request):
    try:
        print("正在计算SVM算法准确率...")
        rate = "%.2f%%" % (get_svm() * 100)
        return HttpResponse(rate)
    except Exception as e:
        print("SVM算法准确率计算失败！错误信息为："+str(e))
        return HttpResponse("ERROR")
