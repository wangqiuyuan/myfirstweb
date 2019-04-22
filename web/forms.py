from django import forms
from .models import Case
from .models import Task

class CaseForm(forms.ModelForm):
    class Meta:
        #使用用例模型来展示表单
        model=Case
        #表单展示内容
        fields=('casename','interfacename','requesturl','method','header','body','checkpoint','relatedtask',)


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        #表单展示内容
        fields=('taskname','player','host',)