from locale import currency
import operator

#paginator and math
from django.core.paginator import Paginator
from django.contrib import messages
import math


from pydoc import pager

from turtle import pos
from django.shortcuts import redirect, render

from .models import Partner, exchange_rate,Operator,Gambia_tax
from tables.models import Charge, Service

from .forms import Countryform,Operatorform,Ratesform,Chargeform,Serviceform


# Create your views here.



# Create your views here.


# Create your views here.



def home(request):



     
     
    operator = Operator.objects.order_by('country_id') # ordering alphabetically with title
    country = Partner.objects.order_by('Country')
    valid = Charge.objects.order_by('Operator')
    clist = list(Partner.objects.values_list('Country',flat=True))
    clist = [c.upper() for c in clist]
    olist = list(Operator.objects.values_list('name',flat=True))
    olist = [o.upper() for o in olist]

    
    #setting up pagination

    p = Paginator(country,10)
    page = request.GET.get('page')
    countries = p.get_page(page)
    

    List = []
    

 #search bar
    
    if(request.POST.get('search')):
     search = request.POST.get('search').upper()
     if search in clist:
         country = Partner.objects.filter(Country=search)
      
         countries = country
         

     elif search in olist:

          operators = Operator.objects.filter(name=search).values_list('country_id',flat=True)
          for o in operators:
               country = Partner.objects.get(Country=o)
               List.append(country)
               countries = List



          

     
  

     else:
          countries = None


    context = {

    'Operator' : operator,
    'Country' : countries,
    'Valid' : valid,
    'Pages' : countries,
   

    }
    
    
    return render(request,"mainpage/index.html",context)







def operator_form(request):

     obj = Partner.objects.order_by('Country')
     Currency= exchange_rate.objects.order_by('LocalCurrency')
     form = Operatorform(request.POST or None)
     olist = list(Operator.objects.values_list('name',flat=True))
     olist = [o.upper() for o in olist]


     if request.method == 'POST':
          form = Operatorform(request.POST)
          operator = request.POST.get('name')
       

          if form.is_valid():
               country = request.POST.get('country')
               currency = request.POST.get('currency')
               operator = request.POST.get('name')
               

               if operator in olist:
                    operator = str(operator.upper()) +  " (" + str(country) + ")"
              
          
   
          
            
               post = form.save(commit=False)
               post.country_id = country 
               post.name = operator 
               
               post.LocalCurrency = currency
               post.save()
               form = post

          

               return redirect('operator_table')

          



     context = {

    'Partner' : obj,
    'form' : form,
    'Currency': Currency

    }
     return render(request,"pages/forms/operator_form.html",context)

    

def service_form(request):

     form = Serviceform(request.POST or None)

     if request.method == 'POST':
          form = Serviceform(request.POST)

          if form.is_valid():
               form.save()

               return redirect('service_form')




               


     context = {
    'form' : form,

    }

     return render(request,"pages/forms/service_form.html",context)


     



def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)




def charge_form(request):
     operators = Operator.objects.order_by('name')
     services = Service.objects.order_by('Service_name')



     form = Chargeform(request.POST or None)


     if request.method == 'POST':
          form = Chargeform(request.POST)
     
        
          operator = request.POST.get('operator')
          service_type = request.POST.get('service_type')
          service_name = request.POST.get('service_name')
          charge = float(request.POST.get('charge'))
  
          currency = Operator.objects.get(name=operator).LocalCurrency
          

          foreign_tax = float(Operator.objects.get(name= operator).foreign_tax)
          GM_tax = float(Gambia_tax.objects.get(pk=1).tax)
          markup = float(Gambia_tax.objects.get(pk=1).markup)
          rate = float(exchange_rate.objects.get(LocalCurrency=currency).rate)


         
          
          if form.is_valid():
      
               post = form.save(commit=False)
               post.Operator = operator
               post.Service_type = service_type
               post.Service = service_name
               
               charge_taxed = (charge * foreign_tax/100) + charge
               charged_GMD = charge_taxed * rate
               if(service_type=='Prepaid'):
                     charged_GMD_taxed = (charged_GMD * GM_tax/100) + charged_GMD

               else:
                    charged_GMD_taxed = charged_GMD

               

               charged_markup = (charged_GMD_taxed * markup/100) + charged_GMD_taxed
               charged_markup = round(charged_markup,2)
               
            
               
               final = normal_round(charged_markup)



               post.calculated = final
               post.save()
               form = post
              


               return redirect('home')
          
        
          
          

     context = {

    'form' : form,
    'Operator': operators,
    'Service' : services,
   

    }
     return render(request,"pages/forms/charge_form.html",context)



def country_form(request):
     rates = exchange_rate.objects.order_by('LocalCurrency')

     form = Countryform(request.POST or None)


     if request.method == 'POST':
          form = Countryform(request.POST)
        
          currency = request.POST.get('currency')
          Country = request.POST.get('Country')
          Country = Country.capitalize()
          
          if form.is_valid():
               post = form.save(commit=False)
               post.LocalCurrency = currency
               post.Country = Country
               post.save()
               form = post
              


               return redirect('operator_form')
          

     context = {

    'form' : form,
    'Currency' : rates,

    }
     return render(request,"pages/forms/country_form.html",context)




def currency_form(request):

     form = Ratesform(request.POST or None)

     if request.method == 'POST':
          form = Ratesform(request.POST)
          name = request.POST.get('LocalCurrency')
          name = name.upper()

          if form.is_valid():
               post = form.save(commit=False)
               post.LocalCurrency = name
               post.save()
               form = post




               return redirect('rate_table')


     context = {
    'form' : form,

    }

     return render(request,"pages/forms/currency_form.html",context)




def register(request):
     return render(request,"pages/samples/register.html",{})

def icons(request):
     return render(request,"pages/icons/mdi.html",{})
     
def tables(request):
     return render(request,"pages/tables/basic-table.html",{})


def buttons(request):
     return render(request,"pages/ui-features/buttons.html",{})


def dropdowns(request):
     return render(request,"pages/ui-features/dropdowns.html",{})


def typography(request):
     return render(request,"pages/ui-features/typography.html",{})


def blank(request, Operators):


     
     prepaid = Charge.objects.filter(Operator = Operators).filter(Service_type = 'Prepaid')
     postpaid = Charge.objects.filter(Operator = Operators).filter(Service_type = 'Postpaid')
     
     

     context = {
          'Postpaid' : postpaid,
          'Prepaid' : prepaid,
    
          'name': Operators,
     }


     return render(request,"pages/samples/blank-page.html",context)

