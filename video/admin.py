from django.contrib import admin

# Register your models here.

# video/admin.py
from django.contrib import admin
from .models import Video

admin.site.register(Video)