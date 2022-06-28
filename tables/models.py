from unittest import TextTestRunner
from django.db import models



class Charge(models.Model):
 
    Operator = models.CharField(max_length=100, blank=True)
    Service_type = models.CharField(max_length=8, blank=True)
    Service = models.CharField(max_length = 100, blank = True)
    charge = models.DecimalField(max_digits=6,decimal_places=2)
    calculated = models.IntegerField(blank=True)

class Service(models.Model):
    Service_name = models.CharField(max_length=100, unique=True);



   

# Create your models here.
