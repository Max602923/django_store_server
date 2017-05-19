from django.shortcuts import render,redirect,HttpResponse
from django.core import serializers
# Create your views here.
from app01 import models
import json
from django.core.serializers.json import DjangoJSONEncoder
def db_handle(request):
    #request 封装了用户请求的所有内容
    #request.POST 用户以POST提交
    #request.GET 用户以GET提交
    #增加
    # models.UserInfo.objects.create(username='alex',password='123',age=73)
    # dic = {
    #     "username":'eric',
    #     "password" : '123',
    #     "age": 73
    # }
    #
    # models.UserInfo.objects.create(**dic)
    #删除
    # models.UserInfo.objects.filter(username='alex').delete()
    #修改
    # models.UserInfo.objects.all().update(age=18)
    #查找
    # models.UserInfo.objects.all()
    # models.UserInfo.objects.filter(age=18).first()

    #queryset 类型的列表
    # for line in user_list_obj:
    #     print(line.username,line.age)
    # data = serializers.serialize('json',user_list_obj)
    # return HttpResponse(data)
    if request.method == "POST":
        print(request.POST)
        # request.POST.get['username']
        # request.POST.get['username']
        # request.POST.get['username']
        # request.POST['age'] = int(request.POST['age'])
        # d = dict(request.POST)
        # models.UserInfo.objects.create(**request.POST)
        # models.UserInfo.objects.create(username = request.POST['username'],
        #                                password = request.POST['password'],
        #                                age = request.POST['age'])

    user_list_obj = models.Author.objects.all()
    # return render(request,'t1.html',{'li':user_list_obj})
    return HttpResponse(serializers.serialize('json',user_list_obj,cls=DjangoJSONEncoder))


def book(request):
    books = models.Book.objects.all()
    publishers = models.Publisher.objects.all();
    authors = models.Author.objects.all()
    print(books)
    return render(request,'t2.html',{'books':books,
                                     'authors':authors,
                                     'publishers':publishers
                                     })


def home(request):
    return HttpResponse("app01.home")

def news(request,nid1,nid2):
    nid = nid1+nid2
    return HttpResponse(nid)
def page(request,n2,n1):
    nid = n1+n2
    return HttpResponse(nid)


def special_case_2003(request):

    return HttpResponse("ok")

