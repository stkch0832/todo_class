from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    return render(request, 'account/index.html')


def register(request):
    user_form = forms.UserCreationForm(request.POST or None)
    if user_form.is_valid():
        try:
            user_form.save()
            return redirect('account:index')
        except ValidationError as e:
            user_form.add_error('password', e)
    return render(request, 'account/register_form.html', context={
        'user_form': user_form,
    })


def user_login(request):
    user_form = forms.UserLoginForm(request.POST or None)

    if request.method == 'POST':
        if user_form.is_valid():
            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password')
            user = authenticate(
                email=email,
                password=password
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'ログインが完了しました')
                    return redirect('account:index')
                else:
                    messages.error(request, 'アカウントがアクティブではありません')
                    return redirect('account:login')
            else:
                messages.error(request, 'アカウントが存在しません')
                return redirect('account:login')
    return render(request, 'account/login_form.html', context={
        'user_form': user_form,
    })


@login_required
def user_logout(request):
    logout(request)
    messages.error(request, 'ログアウトしました')
    return redirect('account:login')
