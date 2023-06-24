from django.shortcuts import render
from collections import UserDict
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth

from django.shortcuts import render, redirect

from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages





# Create your views here.
def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user1=auth.authenticate(username=username,password=password)


        if user1 is not None:
            auth.login(request,user1)
            return redirect('credentials:application')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render (request,"login.html")


def register(request):
   
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,'email taken')
            #     return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname)
                 user.save();
                 print("user createrd")
                 return redirect('credentials:login')
        else:
            messages.info(request,'password not matching')
            return redirect(request,'register')
        return redirect('/') 

    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def application (request):

    return render (request,'application.html')




def applicationform (request):
   if request.method=='POST':
        firstname=request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        DOB=request.POST['DOB']
        Age=request.POST['Age']
        phonenumber=request.POST['phonenumber']
        
        Address=request.POST['Address']

        user2=User.objects.create_user(firstname=firstname,middlename=middlename,last_name=lastname,DOB=DOB,Age=Age,phonenumber=phonenumber, Address= Address)     
        user2.save();
        messages.info(request,'application accepted')
        
        return redirect('/')
   
   

    
   return render(request,'applicationform.html')













