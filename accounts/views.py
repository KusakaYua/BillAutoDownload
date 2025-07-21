from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_view(request):
    """ユーザー新規登録"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '新規登録が完了しました。')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    """ログアウトビュー"""
    logout(request)
    messages.success(request, 'ログアウトしました。')
    return redirect('home')
