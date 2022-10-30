
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('index',views.index),
    path('student',views.studentpage),
    path('company',views.Companydetails),
    path('logout',views.logout_request),
    path('login',views.login_user),
    path('adduser',views.adduser),
    path('shortlist',views.shortlist),
    path('apply/<int:jobid>',views.apply)
    

]
