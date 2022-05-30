"""Django_tutorial URL Configuration

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
from django.contrib import admin
from django.urls import path
from articles import views # __init_.py 파일의 영향으로 'articles' 폴더 자체를 모듈로 인식함

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dinner/<str:name>', views.dinner), # 변수형 URL: 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 방법 (ex. 유저 페이지)
]
