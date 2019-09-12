from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import User, Img
import json
from django.views.decorators.csrf import csrf_exempt
# views视图层，写上请求方法

# 用户登录
@csrf_exempt
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
