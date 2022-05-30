import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name":"족발", "price":30000}, {"name":"햄버거", "price":10000}, {"name":"치킨", "price":20000}, {"name":"피자", "price":20000},]
    pick = random.choice(menus) # random 모듈 사용
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
    } # 데이터를 넘겨줄 때는 보편적으로 context에 담아서 보냄

    return render(request, 'dinner.html', context)