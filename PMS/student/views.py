from sre_constants import BRANCH
from telnetlib import AUTHENTICATION
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
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
    username = request.user.username
    m=Student.objects.filter(roll_no=username).values()
    print(m)
    return render(request,'dashboard.html',{'m':m})
def login_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/index")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')
def studentpage(request):
   
    #return render(request,'dashboard.html') 
    if request.user.is_anonymous:
        return redirect('/login') 
    username = request.user.username
    m=Application.objects.filter(rollno=username).values()
    return render(request,'student.html',{'m':m})
def Companydetails(request):
    if request.user.is_anonymous:
        return redirect('/login')
    company=Company.objects.all().values()
    return render(request,'placements.html',{'n':company}) 
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    #return HttpResponse("logged out")
    return redirect("/")
def adduser(request):
    if request.method=="POST":
        branch=request.POST.get('exampleRadios')
        uname=request.POST.get('rollno')
        emailid=request.POST.get('emailid')
        epassword=request.POST.get('password')
        rollno=request.POST.get('rollno')
        gpa=request.POST.get('gpa')
        name=request.POST.get('name')
        year=request.POST.get('year')
        student = Student(name=name,email=emailid,roll_no=uname,gpa=gpa,course=branch,year=year)
        student.save()



        user = User.objects.create_user(username=uname,
                                 email=emailid,
                                 password=epassword)
        

        print(branch)
        return redirect('/login')
    return render(request,'form.html')

def shortlist(request):
    if request.user.is_anonymous:
        return redirect('/login')
    username = request.user.username
    m=Application.objects.filter(rollno=username).values()
    return render(request,'shortlist.html',{'m':m})

def apply(request):
    if request.POST:
        rollno = request.POST.get('rollno')
        sname = request.POST.get('name')
        company = request.POST.get('cname')
        
        sdetails= Student.objects.filter(roll_no=rollno).values()[0]
        c=Company.objects.filter(name=company).values()[0]
        gpa = sdetails.get('gpa')
        if c.get('cutoff')<=gpa:
            status = "Under Consideration"
        else:
            status = "Rejected"
        application = Application(rollno=rollno,sname=sname,cname=company,status=status,role=c.get('role'))
        application.save()
        return redirect('/shortlist')
    return render(request,'registration.html')


    