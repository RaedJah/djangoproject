from django.forms import ModelForm

from .models import operator_ndcs,exchange_rate,Operator,Partner
from tables.models import Charge,Service,Call_type,HPMNTable
from django_countries.fields import CountryField




class Countryform(ModelForm):
    class Meta:
        model = Partner
        fields = ['Country','Zone','CountryCode']


class Operatorform(ModelForm):
    class Meta:
        model = Operator
        fields = ['name','country_id','standard_iot',
        'mcc_mnc','agreement_type','tadig','foreign_tax','LocalCurrency']
        


class OperatorNDC(ModelForm):
    class Meta:
        model = operator_ndcs
        fields = ['ndc','operator_id']

class Ratesform(ModelForm):
    class Meta:
        model = exchange_rate
        fields = ['LocalCurrency','rate']




class Chargeform(ModelForm):
    class Meta:
        model = Charge
        fields = ['Operator','Service_type','Service','charge','calculated']

class Serviceform(ModelForm):
    class Meta:
        model = Call_type
        fields = ['call_type']


class MainServiceform(ModelForm):
    class Meta:
        model = Service
        fields = ['live']
        
class HPMNServiceform(ModelForm):
    class Meta:
        model = HPMNTable
        fields = ['call_type', 'charge','Service_type']




