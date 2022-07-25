from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


def logoutPage(request,*args,**kwargs):
    logout(request)
    return redirect("login")



def register_user(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            
       

            password2 = request.POST.get('password2')
           
            if(username==None):
                messages.info(request,("Passwords do not match"))
                return redirect('register_user')

            elif(password1!=password2):
                 messages.info(request,("Passwords do not match"))
                 return redirect('register_user')

            else:
                user = authenticate(username=username, password=password1)
              
                usr = User.objects.create_user(username= username)
                usr = User.objects.get(username= username)
                login(request,usr)
            
                usr.set_password(password1)
                usr.save()
             
                messages.success(request,("Registration succesful"))
                return redirect('home')

  

    return render(request,"pages/samples/register.html",{})