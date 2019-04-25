from django import forms
from web.models import Case
from web.models import Task

class CaseForm(forms.ModelForm):
    class Meta:
        #使用用例模型来展示表单
        model=Case
        #表单展示内容
        fields=('casename','interfacename','requesturl','method','header','body','checkpoint','taskid',)


class TaskForm(forms.ModelForm):
    class Meta:
        #使用任务模型来展示表单
        model=Task
        #表单展示内容
        fields=('taskname','player','host',)