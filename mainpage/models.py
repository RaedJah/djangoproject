

from xml.etree.ElementTree import QName
from django.db import models
from django.forms import FloatField


# This contains all models used in the project except for the login and logout page which can be found on 
# Create your models here.


class Partner(models.Model):
    Country = models.CharField(max_length=50, unique=True, null=True)
    CountryCode = models.PositiveIntegerField()
    Zone = models.CharField(blank= True, max_length=100)
  
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    



class Operator(models.Model):
    name = models.CharField(max_length=100)
    country_id = models.CharField(max_length=50, default='Gambia', blank = 'True')
    standard_iot = models.CharField(max_length=1000)
    diot =  models.CharField(max_length=1000)
    mcc_mnc = models.FloatField()
    agreement_type = models.CharField(max_length = 255)
    tadig = models.TextField()
    foreign_tax = models.DecimalField(max_digits=4,decimal_places=2, blank=True)
    LocalCurrency = models.CharField(max_length=3, blank= True, default = 'GMD' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class operator_ndcs(models.Model):
    ndc = models.CharField(max_length=100)
    operator_id = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class exchange_rate(models.Model):
    LocalCurrency = models.CharField(max_length=3, unique=True)
    rate = models.DecimalField(max_digits=6,decimal_places=2)

class Gambia_tax(models.Model):
    tax = models.DecimalField(max_digits=4,decimal_places=2)
    markup = models.DecimalField(max_digits=4,decimal_places=2)