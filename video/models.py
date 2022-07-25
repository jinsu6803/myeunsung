from django.db import models

# Create your models here.

# video/models.py
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_key = models.CharField(max_length=12)
    # 비디오 모델 만들기. 제목, 키 를 저장

