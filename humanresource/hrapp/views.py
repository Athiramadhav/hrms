from django.shortcuts import render
from django.template import Template,loader
from django.http import HttpResponse
from .models import *

# Create your views here.

def userLogin(request):
	template = loader.get_template('login.html')
	try:

		lusername=request.POST.get('username')
		lpassword=request.POST.get('password')
		context={}
		check_user=Register.objects.filter(email=lusername, password=lpassword).exists()
		if check_user:
			login_objs=Login(username=lusername, password=lpassword)
			login_objs.save()
			return render(request, 'home.html',context)
	except Exception as e:
		print(str(e))
		return HttpResponse("login failed")
	return HttpResponse("unsuccessful login")


def registerData(request):
	try:
		vfirstname=request.POST.get('fname')
		vlastname=request.POST.get('lname')
		vage=request.POST.get('age')
		vgender=request.POST.get('gender')
		vplace=request.POST.get('place')
		vemail=request.POST.get('email')
		vpassword=request.POST.get('password')
		check_user_register=Register.objects.filter(email=vemail).exists()
		if check_user_register==False:
			register_obj=Register(firstname=vfirstname, lastname=vlastname, age=vage, gender=vgender, place=vplace,email=vemail, password=vpassword)
			register_obj.save()
			return HttpResponse("Registration done")
	except Exception as e:
		print(str(e))
		return HttpResponse("registration failed try again")
	return HttpResponse("Email or username already exists")
