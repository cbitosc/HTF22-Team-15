from email.policy import default
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models

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
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    cutoff = models.FloatField()
    desc=models.CharField(max_length=500,default='Not available')
    year=models.IntegerField(default=2024)

    def __str__(self) -> str:
        return self.name

