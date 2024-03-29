

#paginator and math
from locale import currency
from logging.config import DEFAULT_LOGGING_CONFIG_PORT
from tokenize import blank_re
from django.core.paginator import Paginator
from django.contrib import messages
import math
from django.shortcuts import redirect
from django.shortcuts import redirect, render

from mainpage.decorators import allowed_user
from .models import Partner, exchange_rate,Operator,Gambia_tax
from tables.models import Charge, Service,Call_type,HPMNTable
from django.contrib.auth.decorators import login_required
from .forms import Countryform,Operatorform,Ratesform,Chargeform,Serviceform,HPMNServiceform,MainServiceform
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page

# Create your views here.


# Create your views here.


# Create your views here.


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def home(request):



    country_list = []
    operator = Operator.objects.order_by('country_id') # ordering alphabetically with title
    country = Partner.objects.order_by('Country')
    valid = Charge.objects.order_by('Operator')
    clist = Partner.objects.all()

    for c in clist:
     country_list.append(c.Country.name)
     country_list = [c.upper() for c in country_list]

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
     if search in country_list:
         
         country = Partner.objects.filter(Country__icontains=search)
         
      
         countries = country
         

     elif search in olist:

          operators = Operator.objects.filter(name=search).values_list('country_id',flat=True)
          for o in operators:
               print(o)
               country = Partner.objects.get(Country__icontains=o)
               
               List.append(country)
               countries = List


     else:
          countries = Partner.objects.filter(Country__icontains=search)



     


    context = {

    'Operator' : operator,
    'Country' : countries,
    'Valid' : valid,
    'Pages' : countries,
   

    }
    
    
    return render(request,"mainpage/index.html",context)



#operator and service function


def customercare(request):



    country_list = []
    operator = Operator.objects.order_by('country_id') # ordering alphabetically with title
    country = Partner.objects.order_by('Country')
    valid = Charge.objects.order_by('Operator')
    clist = Partner.objects.all()

    for c in clist:
     country_list.append(c.Country.name)
     country_list = [c.upper() for c in country_list]

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
     if search in country_list:
         
         country = Partner.objects.filter(Country__icontains=search)
         
      
         countries = country
         

     elif search in olist:

          operators = Operator.objects.filter(name=search).values_list('country_id',flat=True)
          for o in operators:
               print(o)
               country = Partner.objects.get(Country__icontains=o)
               
               List.append(country)
               countries = List


     else:
          countries = Partner.objects.filter(Country__icontains=search)



     


    context = {

    'Operator' : operator,
    'Country' : countries,
    'Valid' : valid,
    'Pages' : countries,

    

    }
    
    
    return render(request,"pages/tables/customercare_view.html",context)



@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect

def operator_form(request):

     obj = Partner.objects.order_by('Country')
     Currency = exchange_rate.objects.order_by('LocalCurrency')
     form = Operatorform(request.POST or None)
     olist = list(Operator.objects.values_list('name',flat=True))
     olist = [o.upper() for o in olist]


     if request.method == 'POST':
          form = Operatorform(request.POST)
          operator = request.POST.get('name')
          
          
       

          if form.is_valid():
               country = request.POST.get('country')
               currency = request.POST.get('currency')
               operator = request.POST.get('name').upper()
               iot = request.POST.get('IOT')
               agreement = request.POST.get('Agreement')
               direction = request.POST.get('direction')

               

               if operator in olist:
                    operator = str(operator.upper()) +  " (" + str(country) + ")"
              
          
   
          
            
               post = form.save(commit=False)
               # if iot=="Discount":
               #      return redirect()
               post.country_id = country 
               post.name = operator 
               post.standard_iot = iot
               post.agreement_type = agreement
               post.direction = direction
               
               post.LocalCurrency = currency
               Service.objects.create(Operator=post.name,Service_name='CAMEL',live=False)
               Service.objects.create(Operator=post.name,Service_name='GPBRS',live=False)
               Service.objects.create(Operator=post.name,Service_name='VOICE',live=False)
               Service.objects.create(Operator=post.name,Service_name='LTE',live=False)

               post.save()
               form = post
          

          

               return redirect('operator_table')

          



     context = {

    'Partner' : obj,
    'form' : form,
    'Currency' : Currency,

    }
     return render(request,"pages/forms/operator_form.html",context)


@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect
def service_form(request):

     form = Serviceform(request.POST or None)

     if request.method == 'POST':
          form = Serviceform(request.POST)

          if form.is_valid():
               form.save()
               return redirect('home')

     context = {

    'form' : form,


    }

 
     return render(request,"pages/forms/service_form.html",context)


@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect
def hpmn_form(request):

     form = HPMNServiceform(request.POST or None)
     call_type = Call_type.objects.order_by('call_type')

     if request.method == 'POST':
          form = HPMNServiceform(request.POST)
          service_type = request.POST.get('service_type')
          call_type = request.POST.get('call_type')
        

          if form.is_valid():
               post = form.save(commit=False)
               post.Service_type = service_type
               post.call_type = call_type
               form = post

               form.save()
               return redirect('home')

     context = {

    'form' : form,
    'Service' : call_type,


    }

 
     return render(request,"pages/forms/hpmn_form.html",context)




@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect
def mainservice_form(request):

     form = MainServiceform(request.POST or None)

     if request.method == 'POST':
          form = MainServiceform(request.POST)

          if form.is_valid():
               form.save()

               return redirect(request.META.get('HTTP_REFERER'))


               


     context = {
    'form' : form,

    }

     return render(request,"pages/forms/mainservice_form.html",context)


     



def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)




@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect
def charge_form(request):
     operators = Operator.objects.order_by('name')
     call_type = Call_type.objects.order_by('call_type')



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
          print(GM_tax)
          markup = float(Gambia_tax.objects.get(pk=1).markup)
          print(markup)
          rate = float(exchange_rate.objects.get(LocalCurrency=currency).rate)
          print(rate)


         
          
          if form.is_valid():
      
               post = form.save(commit=False)
               post.Operator = operator
               post.Service_type = service_type
               post.Service = service_name
            
               if(foreign_tax!= 0):
                    charge_taxed = (charge * foreign_tax/100) + charge
                    

               else:
                    charge_taxed = charge


               



               charged_GMD = charge_taxed * rate
               print(charged_GMD)
               print(charged_GMD)
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
              


               return redirect('blank', Operators=operator,type='VPMN')
          
        
          
          

     context = {



    'form' : form,
    'Operator': operators,
    'Service': call_type,
    
   

    }
     return render(request,"pages/forms/charge_form.html",context)

@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect
def country_form(request):
     rates = exchange_rate.objects.order_by('LocalCurrency')

     form = Countryform(request.POST or None)


     if request.method == 'POST':
          form = Countryform(request.POST)
        
          currency = request.POST.get('currency')
          Country = request.POST.get('Country')
         
          
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


@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect
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


@allowed_user(allowed_roles=['admin'])
@cache_page(60 * 15)
@csrf_protect
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

@allowed_user(allowed_roles=['admin'])
def blank(request, Operators,type):
     
   

     HPMN = HPMNTable.objects.all()
     service = Service.objects.filter(Operator=Operators)
     prepaid = Charge.objects.filter(Operator = Operators).filter(Service_type = 'Prepaid')
     postpaid = Charge.objects.filter(Operator = Operators).filter(Service_type = 'Postpaid')
     country = Operator.objects.get(name=Operators).country_id

     
     operator = Operator.objects.get(name=Operators)
     

   

     if(request.POST.get('search')):
          search = request.POST.get('search').upper()
          prepaid = Charge.objects.filter(Operator = Operators).filter(Service__icontains=search).filter(Service_type = 'Prepaid')
          postpaid = Charge.objects.filter(Operator = Operators).filter(Service__icontains=search).filter(Service_type = 'Postpaid')



     

     context = {
          'Postpaid' : postpaid,
          'Prepaid' : prepaid,
          'operator':operator,
          'type': type,
          'Service':service,
          'HPMN':HPMN,
    
          'name': Operators,
          'country': country
     }


     return render(request,"pages/samples/blank-page.html",context)


def customercare_table(request, Operators,type):
     
   


     service = Service.objects.filter(Operator=Operators)
     prepaid = Charge.objects.filter(Operator = Operators).filter(Service_type = 'Prepaid')
     postpaid = Charge.objects.filter(Operator = Operators).filter(Service_type = 'Postpaid')
     country = Operator.objects.get(name=Operators).country_id
     operator = Operator.objects.get(name=Operators)
     

   

     if(request.POST.get('search')):
          search = request.POST.get('search').upper()
          prepaid = Charge.objects.filter(Operator = Operators).filter(Service__icontains=search).filter(Service_type = 'Prepaid')
          postpaid = Charge.objects.filter(Operator = Operators).filter(Service__icontains=search).filter(Service_type = 'Postpaid')



     

     context = {
          'Postpaid' : postpaid,
          'Prepaid' : prepaid,
          'operator':operator,
          'type': type,
          'Service':service,
    
          'name': Operators,
          'country': country
     }


     return render(request,"pages/samples/customer_table.html",context)