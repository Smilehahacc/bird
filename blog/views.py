from django.http import HttpResponse
from django.http import JsonResponse
from .models import User, Img
import json
import random
from .src.util import zhenzismsclient as smsclient
from blog.src.algorithm.Test import start_sort





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
