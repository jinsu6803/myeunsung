from django.shortcuts import render

# Create your views here.

# django에서의 View는 각종 로직을 처리하는 곳
# Video의 목록 만들기

# video/views.py
from django.shortcuts import render, redirect

from .models import Video # model
from audioop import reverse

def video_list(request):
    video_list = Video.objects.all()
    return render(request, 'video/video_list.html', {'video_list': video_list})


def video_new(request):
    if request.method == 'POST':
        title = request.POST['title']
        video_key = request.POST['video_key']
        Video.objects.create(title=title, video_key=video_key)


        return redirect(reverse('video:list'))
    elif request.method == 'GET':
        return render(request, 'video/video_new.html')


def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video/video_detail.html', {'video': video})
