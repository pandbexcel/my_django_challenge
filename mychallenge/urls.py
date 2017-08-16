from django.conf.urls import include, url
from django.contrib import admin

from people import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/(?P<id>\d+)/', views.list_detail, name='list_detail'),
    url(r'^list/new/$', views.list_new, name='list_new'),
    url(r'^admin/', admin.site.urls),
    
]