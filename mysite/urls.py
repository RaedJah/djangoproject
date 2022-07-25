"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collections import UserList
from django.contrib import admin
from django.urls import path, re_path
from pages.views import loginPage,logoutPage,register_user
from mainpage.views import home,icons,tables,buttons,dropdowns,typography,blank,customercare
from mainpage.views import operator_form,hpmn_form,country_form,currency_form,charge_form,service_form,mainservice_form,customercare_table
from tables.views import country_table, delete_charge,operator_table,rate_table, export_excel,charge_table,delete_operator, update_mainservice,update_operator,update_currency
from tables.views import delete_charge

urlpatterns = [

#MAIN

    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('customercare',customercare,name="customercare"),

#FORMS

    path('operator_form', operator_form, name="operator_form"),
    path('country_form', country_form, name="country_form"),
    path('currency_form', currency_form, name="currency_form"),
  
    path('charge_form',charge_form, name="charge_form"),
    path('service_form',service_form, name="service_form"),
    path('hpmn_form',hpmn_form, name= "hpmn_form"),

    path('mainservice_form',mainservice_form, name="mainservice_form"),


 



#NAVBAR

    # path('charts', charts, name="charts"),
    path('register', register_user, name="register_user"),
    path('icons', icons, name="icons"),
    path('tables', tables, name="tables"),
    path('buttons', buttons, name="buttons"),
    path('dropdowns', dropdowns, name="dropdowns"),
    path('typography', typography, name="typography"),
    path('login',loginPage, name ='login'),
    path('logout',logoutPage,name = 'logout'),

    #TABLES

    path('country_table', country_table, name="country_table"),
    path('operator_table', operator_table, name="operator_table"),
    path('rate_table', rate_table, name="rate_table"),
    path('charge_table/<type>', charge_table, name="charge_table"),


    #EXCEL


    path('export_excel',export_excel, name="export_excel"),


    #DELETE/UPDATE

    path('delete_operator/<Operators>',delete_operator,name='delete_operator'),
    path('update_operator/<Operators>',update_operator,name='update_operator'),
    path('update_currency/<curr>',update_currency,name='update_currency'),
    path('delete_charge/<Charges>',delete_charge,name='delete_charge'),
    path('update_mainservice/<Operators>/<service>',update_mainservice,name='update_mainservice' ),











   
    # path('operator/<Operators>/<type>',blank,name='blank'),
    path('operator/<Operators>/<type>',customercare_table,name='ccare'),
    path('operators/<Operators>/<type>',blank,name='blank'),

    # path('')

    
    
   



]

