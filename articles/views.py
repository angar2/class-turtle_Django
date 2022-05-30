import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = ['족발', '햄버거', '피자', '치킨']
    pick = random.choice(menus) # random 모듈 사용
    context = {
        'pick': pick,
        'name': name,
    } # 데이터를 넘겨줄 때는 보편적으로 context에 담아서 보냄

    return render(request, 'dinner.html', context)