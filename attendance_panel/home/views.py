from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
import csv
from .models import *

def home(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=venues.csv'
	
	# Create a csv writer
	writer = csv.writer(response)

	# Designate The Model
	stu = Student.objects.all()

	# Add column headings to the csv file
	writer.writerow(['name', 'email', 'studied', 'address', 'attendance'])

	# Loop Thu and output
	for s in stu:
		writer.writerow([s.name, s.email, s.studied, s.address, s.attendance])

	return response

# def signup(request):

#     if request.method=="POST":
#         Email=request.POST['email']
#         Password=request.POST['password']
     
#         if User.objects.filter(email=Email).exists():
#             messages.error(request,'Email already exists')
#             return render(request,"signup.html")
#         else:
#             User.objects.create(email=Email,password=Password)
#             messages.success(request,'Successfully registered')
#             return redirect("/")
#     else:
#         return render(request,'signup.html')

# def signin(request):
#     if request.method=='POST':
#         email=request.POST['email']
#         password=request.POST['password']
#         user=auth.authenticate(email=email,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return render(request,'home.html')
#         else:
#             messages.info(request,"Invalid username or password")
#             return render(request,'home.html')
#     else:
#         return render(request,'home.html')

