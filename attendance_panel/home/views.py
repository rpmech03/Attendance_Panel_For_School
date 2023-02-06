from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

def signup(request):

    if request.method=="POST":
        Email=request.POST['email']
        Password=request.POST['password']
     
        if User.objects.filter(email=Email).exists():
            messages.error(request,'Email already exists')
            return render(request,"signup.html")
        else:
            User.objects.create(email=Email,password=Password)
            messages.success(request,'Successfully registered')
            return redirect("/")
    else:
        return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            messages.info(request,"Invalid username or password")
            return render(request,'home.html')
    else:
        return render(request,'home.html')

