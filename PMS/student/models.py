from email.policy import default
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime  
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_no = models.BigIntegerField()
    gpa = models.FloatField()
    course = models.CharField(max_length=100)
    year=models.IntegerField(default=2024)
    

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    jobid = models.IntegerField()
    name = models.CharField(max_length=100)
    date=models.DateField(default=datetime.now())
    cutoff = models.FloatField()
    year=models.IntegerField()
    package=models.FloatField(default=5.6)
    role=models.CharField(max_length=100,default='Not available')
    desc=models.CharField(max_length=500,default='Not available')

    


    def __str__(self) -> str:
        return self.name

class Application(models.Model):
    rollno=models.IntegerField()
    sname=models.CharField(max_length=100)
    cname = models.CharField(max_length=100)
    status=models.CharField(max_length=50)

    def __str__(self):
        return str(self.sname)+"-"+str(self.cname)
    