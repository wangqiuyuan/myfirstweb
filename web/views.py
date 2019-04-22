#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from .models import User
from django.views.decorators.csrf import csrf_exempt
from .forms import CaseForm
from .models import Case
from .models import Task
from .forms import TaskForm
import pymysql



#登陆
@csrf_exempt

def login(request):
    if request.method == 'POST':
        #获取表单用户密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        #获取的表单数据与数据库进行比较
        user = User.objects.filter(username__exact=username,password__exact=password)
        if user:
            #比较成功，跳转index
            response = HttpResponseRedirect('/manager/')
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('username',username,3600)
            return response
        else:
            #比较失败，还在login
            return HttpResponseRedirect('/admin/')
    # else:
    #     uf = UserForm()
    return render(request, 'index.html', )

#登陆成功
@csrf_exempt
def manager(request):
    return render(request,'web/dashboard.html')

#登录失败
@csrf_exempt
def admin(request):
    return render(request,'index.html')

#退出
def logout(request):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response
#任务
@csrf_exempt
def task(request):
    tasksuits=Task.objects.all()
    print(tasksuits)
    return render(request,'task.html',{'tasksuits':tasksuits})

#删除任务
@csrf_exempt
def deltask(request):
    id=request.GET.get('id')
    print(id)
    Task.objects.filter(id=id).delete()
    return HttpResponseRedirect('/task/')

#创建用例
@csrf_exempt
def createcase(request):
    if request.method == 'POST':
        print("提交了")
        #获取用例信息
        caseinfos=CaseForm(request.POST)
        #判断用例提交是否有效
        if caseinfos.is_valid():
            print("提交有效")
            print(caseinfos.cleaned_data)
            caseinfos.save()
            return HttpResponseRedirect('/case/')
        else:
            print("提交数据无效")
            print(caseinfos.cleaned_data)
            print(caseinfos.errors)
            return render(request, 'interfaceform.html')
    else:
        caseinfos=CaseForm()
        return render(request,'interfaceform.html',{'caseinfos':caseinfos})

#报告
@csrf_exempt
def report(request):
    return render(request,'report.html')

#用例
@csrf_exempt
def case(request):
    casesuits=Case.objects.all()
    print(casesuits)
    return render(request, 'case.html', {'casesuits': casesuits})

#删除用例
@csrf_exempt
def delcase(request):
    id=request.GET.get('id')
    print(id)
    Case.objects.filter(id=id).delete()
    return HttpResponseRedirect('/case/')

#创建任务
@csrf_exempt
def createtask(request):
    if request.method=='POST':
        print('提交了')
        #获取任务信息
        taskinfo=TaskForm(request.POST)
        if taskinfo.is_valid():
            print("提交有效")
            print(taskinfo.cleaned_data)
            taskinfo.save()
            return HttpResponseRedirect('/task/')
        else:
            print("提交无效")
            print(taskinfo.cleaned_data)
            print(taskinfo.errors)
    taskinfo=TaskForm()
    return render(request,'createtask.html',{'taskinfo':taskinfo})

#报告详情
@csrf_exempt
def detailreport(request):
    return render(request,'detailreport.html')