from datetime import datetime
from http.client import HTTPResponse
from locale import currency
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from mainpage.models import Partner, exchange_rate,Operator,operator_ndcs
from .models import Charge
import xlwt
from mainpage.forms import Countryform, Operatorform, Ratesform
from django.shortcuts import redirect





# Create your views here.

def country_table(request):
    
     obj = Partner.objects.order_by('Country')

     

     if(request.POST.get('search')):
          search = request.POST.get('search').upper()
         
          obj = Partner.objects.filter(Country__icontains=search)





     
     context = {

    'Country' : obj,
    }
     return render(request,"pages/tables/countries.html",context)
     

def operator_table(request):
     country_list = []
     clist = Partner.objects.all()
    
     for c in clist:
          country_list.append(c.Country.name)
          country_list = [c.upper() for c in country_list]
     obj = Operator.objects.order_by('name')
     olist = list(Operator.objects.values_list('name',flat=True))
     olist = [o.upper() for o in olist]


     if(request.POST.get('search')):
          search = request.POST.get('search').upper()
          if search in olist:
               obj = Operator.objects.filter(name=search)


          elif search in country_list:
                obj = Operator.objects.filter(country_id=search)

          else:
                  obj = Operator.objects.filter(name__icontains=search)
         
               

     





     context = {

    'Operator' : obj ,
    }

     return render(request,"pages/tables/operators.html",context)


def rate_table(request):
     obj = exchange_rate.objects.order_by('LocalCurrency')
     curr = 'Currency'


     if(request.POST.get('search')):
          search = request.POST.get('search').upper()

          obj = exchange_rate.objects.filter(LocalCurrency__icontains=search)

     context = {
    'tagline': curr,

    'Rate' : obj ,
    }



     return render(request,"pages/tables/exchange_rate.html",context)
     



def delete_operator(request,Operators):
   
     lent = (len(Operators))-1
     print(Operators)
     iD = Operators[17:lent]

     operator = Operator.objects.get(id=int(iD))
     
  
     
     if request.method=='POST':

          operator.delete()
          charge = Charge.objects.filter(Operator=operator.name)
          for c in charge:
               c.delete()
          
          return redirect('operator_table')


     context = {

     'obj' : operator.name ,
    }



     return render(request,"pages/forms/delete_form.html",context)
    


def delete_charge(request,Charges):
     lent = (len(Charges))-1
     iD = Charges[15:lent]

     charge = Charge.objects.get(id=int(iD))


     
     
     if request.method=='POST':

          charge.delete()

          
          return redirect('home')


     context = {

     'obj' : charge.Service ,
    }



     return render(request,"pages/forms/delete_form.html",context)

def update_currency(request,curr):
   
     currency = exchange_rate.objects.get(LocalCurrency =curr)

     operator = Operator.objects.filter(LocalCurrency=curr)
     form = Ratesform(instance= currency)
     

     if request.method=='POST':

          form = Ratesform(request.POST,instance= currency)
          name = request.POST.get('LocalCurrency')
          name = name.upper()
          if form.is_valid():
               post = form.save(commit=False)
               post.LocalCurrency = name
               post.save()
               
               currency = request.POST.get('LocalCurrency')
               form = post
               for c in operator:
                    c.LocalCurrency = currency
            
                    c.save()

     
               return redirect('rate_table')



     context = {
    'form' : form,


    }
     return render(request,"pages/forms/currency_form.html",context)




def update_operator(request,Operators):
     obj = Partner.objects.order_by('Country')
     operator = Operator.objects.get(name=Operators)
     form = Operatorform(instance= operator)
     Currency= exchange_rate.objects.order_by('LocalCurrency')

     if request.method=='POST':

          form = Operatorform(request.POST,instance= operator)
          if form.is_valid():
               country = request.POST.get('country')
               currency = request.POST.get('currency')
               operator = request.POST.get('name')
               iot = request.POST.get('IOT')
               agreement = request.POST.get('Agreement')
               
               
       
               post = form.save(commit=False)
               post.country_id = country 
               post.name = operator 
               post.standard_iot = iot
               post.LocalCurrency = currency
               post.agreement_type = agreement

               post.save()
               form = post

          

               return redirect('operator_table')



     context = {

    'Partner' : obj,
    'Currency' : Currency,
    'form' : form,

    }
     return render(request,"pages/forms/operator_form.html",context)




def charge_table(request,type):
    
     obj =  Charge.objects.order_by('Operator')
     obj2 = Operator.objects.order_by('name')


     olist = list(Charge.objects.values_list('Operator',flat=True))
     olist = [o.upper() for o in olist]

     if(request.POST.get('search')):
          search = request.POST.get('search').upper()
          if search in olist:
               obj = Charge.objects.filter(Operator=search)


     context = {
    'Operator': obj2,
    'type':type,

    'Charge' : obj ,
    }



     return render(request,"pages/tables/charge-table.html",context)
     


def export_excel(request):

     response = HttpResponse(content_type='application/ms-excel')
     response['Content-Disposition'] = 'attachment;  filename="Charges.xls"' 
     
     wb = xlwt.Workbook(encoding='utf-8')
     ws = wb.add_sheet('Charge')
     row_num = 0
     font_style = xlwt.XFStyle()
     font_style.font.bold = True
     


     columns=['Opertaor', 'Service Type', 'Service','Amount','Final Charge']

     for col_num in range(len(columns)):
          ws.write(row_num,col_num,columns[col_num],font_style)

     font_style = xlwt.XFStyle()

     rows = Charge.objects.all().values_list('Operator','Service_type','Service','charge','calculated')

     for row in rows:

          row_num +=1

          for col_num in range(len(row)):
               ws.write(row_num,col_num,str(row[col_num]),font_style)

     wb.save(response)

     return response

    



 

