"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import eunsunghome.views




urlpatterns = [
    path('admin/', admin.site.urls),

    path('common/', include('common.urls')),
    # common 앱의 urls.py 파일을 사용(http://localhost:8000/common/ 으로 시작하는 URL은 모두 common/urls.py 파일을 참조)
    path('', eunsunghome.views.index, name='index'),
    path('index_video/', eunsunghome.views.index_video, name='index_video'),
    path('video/', include('video.urls'), name='video'),
    path('pybo/',  include('pybo.urls')),
    path('Lidar/',  include('Lidar.urls'))


    #  ''의 의미는 우리가 만든 블로그 홈페이지의 주소를 입력할 때 아무것도 입력하지 않았다는 의미
    # eunsunghome.views.index는 우리가 만든 index 함수를 적용
    #  name='index'는 위에 초록색으로 글씨 써있는 부분에 보면, 함수를 적용시키고 이름을 명명하게 되면 나중에 html 파일에서 이 값으로 url 값을 불러올 수가 있ek
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)