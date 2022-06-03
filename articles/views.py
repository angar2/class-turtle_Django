import random
from django.shortcuts import render

# Create your views here.
def index(request): # request: 요청의 모든 정보를 담고 있는 변수
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

def review(request):
    return render(request, 'review.html')

def create_review(request):
    content = request.POST.get('content') # html에서 name이 'content'인 input의 값
    print(request)
    context = {
        'content': content,
    }
    return render(request, 'review_result.html', context)