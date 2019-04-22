from django.conf.urls import url,include

from web import views
import web

urlpatterns = [
    url(r'^$',views.admin),
    url(r'^$',views.manager),
    url(r'^$',views.login),
    url(r'^$',views.task),
    url(r'^$',views.case),
    url(r'^$',views.report),
    url(r'^$',views.createcase),
    url(r'^$',views.createtask),
    url(r'^$',views.detailreport),
    url(r'^$',views.delcase),
    url(r'^$',views.task),

]