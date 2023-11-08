from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            
            # http://127.0.0.1:8000/accounts/login/ => None
            # http://127.0.0.1:8000/accounts/login/?next=/articles/create/ => 'articles/create'
            next_url = request.GET.get('next')

            return redirect(next_url or 'articles:index')
            # next 인자에 url이 있을 때 => 'articles/create/' or 'articles:index' => 'articles/create/' 리턴
            # next 인자에 url이 없을 때 => None or 'articles:index' => 'articles:index'
    
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
