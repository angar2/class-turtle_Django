from django.urls import path
from articles import views

app_name = 'articles' # 앱의 이름을 지정함
urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>', views.dinner), # 변수형 URL: 주소 자체를 변수처럼 사용해서 동적으로 주소를 만드는 방법 (ex. 유저 페이지)
    path('review/', views.review, name='review'), # name: 명시한 이름으로 알아서 주소를 찾아줌
    path('create_review/', views.create_review, name='create_review'),
]
    