from unittest import TextTestRunner
from django.db import models
from django import forms
from datetime import datetime



class Charge(models.Model):
 
    Operator = models.CharField(max_length=100, blank=True)
    Service_type = models.CharField(max_length=8, blank=True)
    Service = models.CharField(max_length = 100, blank = True)
    charge = models.DecimalField(max_digits=6,decimal_places=2)
    calculated = models.DecimalField(max_digits=6,decimal_places=2,blank= True)

class Service(models.Model):
    Operator = models.CharField(max_length=100,blank=True)
    Service_name = models.CharField(max_length=100);
    live = models.BooleanField();
    live_on = models.DateField(auto_now_add=False,blank=True,default=datetime.now)



class HPMNTable(models.Model):
    call_type = models.CharField(max_length=100);
    charge  = models.DecimalField(max_digits=6,decimal_places=2)
    Service_type = models.CharField(max_length=8, blank=True)



class Call_type(models.Model):
    call_type = models.CharField(max_length=100, unique=True);
    



class Diot(models.Model):

    operator = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=6,decimal_places=2)

# Create your models here.
