from django.shortcuts import render

# Create your views here.
def index(request):
    lunch = [
        '짜장면',
        '탕수육',
        '짬뽕',
    ]
    context = {
        'lunch': lunch,
    }
    return render(request, 'index.html', context)

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # print(dir(request))
    user_id = request.GET.get('id')
    user_pw = request.GET.get('pw')
    # 로그인 했다고 가정. model 을 알고 나면, 회원가입, 로그인 등이 가능해질것.
    context = {
        'user_id': user_id,
    }
    return render(request, 'pong.html', context)

def detail(request, num):

    articles = [
        '게시물1',
        '게시물2',
        '게시물3',
    ]
    
    result = articles[num-1]

    context = {
        'result': result
    }
    return render(request, 'detail.html', context)