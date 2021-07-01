from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User   # user에 대한 클래스를 가져와준다.
from django.contrib import auth               # 계정에 대한 권한에 대한 것을 가져와준다.

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #auth.authenticate 라는 말은 DB에서 방금전에 입력한 이 내용이 우리한테 있는 회원명단이 맞는지 확인시켜주는 함수
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:    # is not None = None이 아니라면 = 회원이라면
            auth.login(request,user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('main')
    return render(request,'login.html')