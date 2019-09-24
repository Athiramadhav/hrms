from django.shortcuts import render
from django.template import Template,loader
from django.http import HttpResponse
from .models import *

# Create your views here.

def userLogin(request):
	template = loader.get_template('login.html')
	context={}
	return HttpResponse(template.render(context,request))
	try:
		if request.method == 'POST':
			lusername = request.POST.get('username')
			lpassword = request.POST.get('password')
			check_user=Login.objects.get(username=lusername, password=lpassword)
			return render(request,'admin_home.html')
		except Exception as e:
			print(str(e))
			return HttpResponse("login failed")
		return render(request, 'login.html')


def registration(request):
	try:
		if request.method=='POST':
			vupload_image = request.FILE['file_upload']
			vfname = request.Post.get('emp_firstname')
			vlname = request.Post.get('emp_lastname')
			vgender = request.Post.get('emp_gender')
			vdob = request.Post.get('emp_dob')
			vaddress = request.Post.get('emp_address')
			vphone =request.Post.get('emp_mobileno')
			vemail = request.Post.get('emp_email')
			vpassword = request.Post.get('emp_password')
			vdesignation = request.Post.get('emp_designation')
			vqualification = request.Post.get('emp_qualification')
			vexperience = request.Post.get('emp_experience')
			vsalary = request.Post.get('emp_salary')
			vjoin_date = request.Post.get('emp_joindt')
			emp_detail = EmployeeProfile(upload_image=vupload_image,fname=vfname,lname=vlname,gender=vgender,dob=vdob,address=vaddress,
				phone=vphone,email=vemail,password=vpassword,designation=vdesignation,emp_qualification=vqualification,emp_experience=vexperience,
				salary=vsalary,join_date=vjoin_date)
			return HttpResponse('registration successfull')
	except Exception as e:
		print(str(e))
		return HttpResponse('registration failed')


def candidateRegistration(request):
	try:
		if request.method=='POST':
			var_candidate_name = request.POST.get('candidatename')
			var_dob = request.POST.get('dob')
			var_address = request.POST.get('address')
			var_phone_no = request.POST.get('mobileno')
			var_gender = request.POST.get('gender')
			var_qualification = request.POST.get('qualification')
			var_year_of_pass = request.POST.get('yrofpass')
			var_experience = request.POST.get('experience')
			var_email = request.POST.get('email')
			var_password = request.POST.get('password')
			upload_resume = request.FILE['file_upload']
			candidate_detail = Candidate(candidate_name=var_candidate_name,dob=var_dob,address=var_address,phone_no=var_phone_no,
				gender=var_gender,qualification=var_qualification,year_of_pass=var_year_of_pass,experience=var_experience,email=var_email,
				password=var_password)
	except Exception as e:
		print(e)

