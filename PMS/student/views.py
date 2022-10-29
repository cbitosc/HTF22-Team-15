from telnetlib import AUTHENTICATION
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            return redirect('/')
        else:
            return render(request,'index.html')
    return render(request,'login.html')
def logout_view(request):
    logout(request)
    return redirect('/login')
    