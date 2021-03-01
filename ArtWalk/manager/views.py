from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        User_form = UserCreationForm(request.POST)
        Profile_form = ProfileForm(request.POST)
        if User_form.is_valid() and Profile_form.is_valid():
            user = User_form.save()
            auth_login(request, user)
            user.save()
            profile = Profile_form.save()
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        User_form = UserCreationForm()
        Profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': User_form, 'profile_form':Profile_form})
