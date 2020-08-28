from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login

def login(request):
    context = dict()
    return render(request, login.html)

def profile(request):
    context = dict()
    return render(request, 'profile.html', context)
