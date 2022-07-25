# video/urls.py
from django.urls import path
from django.conf.urls import include
from . import views

from . import views
from django.urls import path, include

urlpatterns = [
    path('/', views.video_list, name='list'),

    path('/', views.video_new, name='new'), #/video/new 경로로 들어가면 사용자에게 입력받을 수 있게끔 연결

    path('/', views.video_detail, name='detail'),
]