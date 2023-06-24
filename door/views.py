from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile

def door(request):
    return render(request, 'registration/door.html')

def fail(request):
    return render(request, 'registration/fail.html')

def login(request):
    return render(request, 'registration/login.html')



def reg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/game')
    else:
        form = SignUpForm()
    return render(request, 'registration/reg.html', {'form': form})