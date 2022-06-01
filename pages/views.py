from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.

def home(request):
     return render(request,"home_page/home.html",{})



def loginPage(request,*args,**kwargs):

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password = password)
        if(user is not None):
            login(request,user)
            return redirect('home')

        else:
            messages.info(request, 'Email or Password is incorrect')
   

    return render(request,"login/login.html",{})


