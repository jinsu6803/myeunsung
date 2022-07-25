from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'eunsunghome/index.html')

def index_video(request):
    return render(request, 'eunsunghome/index_video.html')

def some_function(request):
    ...
    messages.warning(request, "권한이 없습니다.")
    ...