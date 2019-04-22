from django.db import models
from django.utils import  timezone


# 登录
class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)



    def __unicode__(self):
        return self.username

#用例模型
class Case(models.Model):
    casename=models.CharField(max_length=50)
    interfacename=models.CharField(max_length=50)
    requesturl=models.URLField()
    method=models.CharField(max_length=50)
    header=models.TextField()
    body=models.TextField()
    relparameter=models.TextField()
    checkpoint=models.TextField()
    relatedtask = models.TextField(null=True)
    createtime=models.DateField(auto_now_add=True)

    def _unicode_(self):
        return self.casename

#任务模型
class Task(models.Model):
    taskname=models.CharField(max_length=50)
    player=models.EmailField()
    host=models.CharField(max_length=50)
    state=models.IntegerField(null=True)
    extime=models.DateTimeField(auto_now_add=True)
    createtime=models.DateTimeField(auto_now_add=True)


    def _unicode_(self):
        return self.taskname
