from django.urls import path
from articles import views


urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>', views.dinner), # 변수형 URL: 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 방법 (ex. 유저 페이지)
    path('review/', views.review),
    path('create_review/', views.create_review),
]
    