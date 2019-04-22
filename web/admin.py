from django.contrib import admin
from .models import User
from .models import Case

#注册模型
admin.site.register(User)
admin.site.register(Case)
