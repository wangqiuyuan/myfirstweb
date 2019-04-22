from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path,include
from web.views import login
from web.views import manager
from web.views import task
from web.views import case
from web.views import report
from web.views import createcase
from web.views import createtask
from web.views import detailreport
from web.views import admin
from web.views import delcase
from web.views import deltask

urlpatterns = [
    path(r'admin/',admin),
    path(r'login/',login),
    path(r'web/', include('web.urls')),
    path(r'task/',task),
    path(r'case/',case),
    path(r'report/',report),
    path(r'manager/',manager),
    path(r'createcase/',createcase),
    path(r'createtask/',createtask),
    path(r'detailreport/',detailreport),
    path(r'delcase/',delcase),
    path(r'deltask/',deltask)

]
