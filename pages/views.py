from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from mainpage.decorators import unauthenticated_user


@cache_page(60 * 15)
@csrf_protect
@unauthenticated_user
def loginPage(request,*args,**kwargs):
    

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password = password)
        if(user is not None):



                login(request,user)

                if user.groups.filter(name='admin'):
                        print('yes')
                        return redirect('home')
                else:
                     return redirect('customercare')


        else:
            messages.info(request, 'Email or Password is incorrect')
   

    return render(request,"login/login.html",{})

@cache_page(60 * 15)
@csrf_protect
def logoutPage(request,*args,**kwargs):
    logout(request)
    return redirect("login")


@cache_page(60 * 15)
@csrf_protect
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
                
                usr = User.objects.create_user(username= username)
                usr = User.objects.get(username= username)
                login(request,usr)

            
                usr.set_password(password1)
                usr.save()
                usr.set_password(usr.password)
                usr.save()
            
                messages.success(request,("Registration succesful"))
                return redirect('customercare')

    

    return render(request,"pages/samples/register.html",{})