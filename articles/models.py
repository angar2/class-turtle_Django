from django.db import models

# Create your models here.
class Articles(models.Model): # 상속: dajango에서 제공하는 Model의 설정법을 가져와서 사용
    
    # id는 자동으로 부여됨
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add: 생성 시 현재 시간을 자동 추가
