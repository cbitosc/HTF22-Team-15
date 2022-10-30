from telnetlib import AUTHENTICATION
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'home.html')

#bala's code
def home(request):
    if request.POST :
        sname = request.POST['name']
        mail = request.POST['email']
        gpa = request.POST['gpa']
        course = request.POST['course']
        temp = []
        companies = Company.objects.all()
        for i in range(len(companies)):
            # the student who has more gpa than cutoff will be shortlisted and that 
            # companies names are added to temp variable
            if companies[i].cutoff <= gpa:
                temp.append(companies[i].name)
        #returning the companies he got shorlisted.
        return render('index.html', {'shortlist':temp})
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'login.html')
def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form=AuthenticationForm()
    return render(request,'login.html')

def studentpage(request):
    m=Student.objects.all()
    return render(request,'student.html',{'m':m})  
def Companydetails(request):
    company=Company.objects.all()
    return render(request,'student.html',{'n':company}) 
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

    