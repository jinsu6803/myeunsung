from django.conf.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('detectme', views.detectme, name="detectme"),
    path('lidar_detectme', views.lidar_detectme, name="lidar_detectme"),
]