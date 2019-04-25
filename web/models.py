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
    taskid = models.IntegerField(null=True)
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
    caseid=models.IntegerField(null=True)
    createtime=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.taskname

#报告模型
class Report(models.Model):
    taskid=models.IntegerField()
    casenumber=models.IntegerField()
    passnumber=models.IntegerField()
    failnumber=models.IntegerField()
    passrate=models.FloatField()
    createtime=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.taskid

#执行记录
class Record(models.Model):
    reportid=models.IntegerField()
    taskid=models.IntegerField()
    caseid=models.IntegerField()
    casestate=models.IntegerField()
    requestinfo=models.TextField()
    log=models.TextField()
    createtime=models.DateTimeField(auto_now_add=True)


    def _unicode_(self):
        return self.reportid
