from django.shortcuts import render, redirect
from django.template import Template,loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.

def userLogin(request):
	#template = loader.get_template('login.html')
	#context={}
	#return HttpResponse(template.render(context,request))
	try:
		if request.method == 'POST':
			lusername = request.POST.get('username')
			print(lusername)
			lpassword = request.POST.get('password')
			print(lpassword)
			check_user=EmployeeProfile.objects.get(email=lusername, password=lpassword)
			if check_user:
				login_obj = Login(username=lusername, password=lpassword)
				login_obj.save()
				return render(request,'hr_home.html')
		return render(request,'login.html')
	except Exception as e:
			print(str(e))
			return render(request, 'login.html')

def home(request):
	try:
		return render(request,'hr_home.html')
	except Exception as e:
		print(str(e))



def registration(request):
	if request.method=='POST' and request.FILES['file_upload']:
		try:
			vupload_image = request.FILES['file_upload']
			vfname = request.POST.get('emp_firstname')
			vlname = request.POST.get('emp_lastname')
			vgender = request.POST.get('emp_gender')
			vdob = request.POST.get('emp_dob')
			vaddress = request.POST.get('emp_address')
			vphone =request.POST.get('emp_mobileno')
			vemail = request.POST.get('emp_email')
			vpassword = request.POST.get('emp_password')
			vdesignation = request.POST.get('emp_designation')
			vqualification = request.POST.get('emp_qualification')
			vexperience = request.POST.get('emp_experience')
			vsalary = request.POST.get('emp_salary')
			vjoin_date = request.POST.get('emp_joindt')
			check_user_register=EmployeeProfile.objects.filter(email=vemail).exists()
			if check_user_register==False:
				emp_detail = EmployeeProfile(upload_image=vupload_image,fname=vfname,lname=vlname,gender=vgender,dob=vdob,address=vaddress,
				phone=vphone,email=vemail,password=vpassword,designation=vdesignation,emp_qualification=vqualification,emp_experience=vexperience,
				salary=vsalary,join_date=vjoin_date)
				emp_detail.save()
				return HttpResponse('registration succecssful')
				return render(request,'employee_registration.html')
		except Exception as e:
			print(str(e))
			return HttpResponse('registration failed')
	return render(request, 'employee_registration.html')


def employeeDetail(request):
	user_objs = EmployeeProfile.objects.all()
	user=[]
	context={}
	for user_obj in user_objs:
		user.append(user_obj.upload_image)
		user.append(user_obj.fname)
		user.append(user_obj.lname)
		user.append(user_obj.gender)
		user.append(user_obj.dob)
		user.append(user_obj.adress)
		user.append(user_obj.phone)
		user.append(user_obj.email)
		user.append(user_obj.password)
		user.append(user_obj.designation)
		user.append(user_obj.emp_qualification)
		user.append(user_obj.salary)
		user.append(user_obj.join_date)
	context={'userlist':user_objs}
	return render(request, 'employee_deatil.html',context)


def addQuestion(request):
	try:
		if request.method=='POST':
			val_question = request.POST.get('question')
			val_option1 = request.POST.get('option1')
			val_option2 = request.POST.get('option2')
			val_option3 = request.POST.get('option3')
			val_option4 = request.POST.get('option4')
			val_ans = request.POSTget('answer')
			exam_object = QuestionPaper(question=val_question, option1=val_option1, option2=val_option2, option3=val_option3, option4=val_option4, answer=val_ans)
			exam_object.save()
			return HttpResponse('saved')
	except Exception as e:
		print(str(e))
		return HttpResponse('not saved')


def candidateRegistration(request):
	if request.method == 'POST':
		try:
			var_candidate_name = request.POST.get('candidatename')
			print(var_candidate_name)
			var_dob = request.POST.get('dob')
			print(var_dob)
			var_address = request.POST.get('address')
			print(var_address)
			var_phone_no = request.POST.get('mobileno')
			print(var_phone_no)
			var_gender = request.POST.get('gender')
			print(var_gender)
			var_qualification = request.POST.get('qualification')
			print(var_qualification)
			var_year_of_pass = request.POST.get('yrofpass')
			print(var_year_of_pass)
			var_experience = request.POST.get('experience')
			print(var_experience)
			var_email = request.POST.get('email')
			print(var_email)
			var_password = request.POST.get('password')
			print(var_password)
			upload_resume = request.FILES['file_upload']
			candidate_detail = Candidate(candidate_name=var_candidate_name,dob=var_dob,address=var_address,phone_no=var_phone_no,
				               gender=var_gender,qualification=var_qualification,year_of_pass=var_year_of_pass,experience=var_experience,email=var_email,
				               password=var_password)
			candidate_detail.save()	
			resume_detail = Resume(resume='upload_resume',fk_candidate_id=candidate_detail)
			return HttpResponse('Registerd')
		except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'candidate_registration.html')


def complaintReg(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			ename = request.POST.get('name')
			eid = request.POST.get('id')
			edesg = request.POST.get('post')
			edept = request.POST.get('dept')
			eaddress = request.POST.get('addr')
			ephone = request.POST.get('phone')
			cname = request.POST.get('compname')
			cdesg = request.POST.get('cpost')
			cdept = request.POST.get('cdept')
			cact =request.POST.get('act')
			date = request.POST.get('date')
			time = request.POST.get('time')
			comp_reg = Complaint(e_name=ename, e_desgination=edesg, e_dept=edept, e_addr=eaddress,
			           e_phone=ephone, c_name=cname, complaint_desg=cdesg, complaint_dept=cdept,
			           compaint_description=cact, date_of_incident=date, time_of_incident=time)
			comp_reg.save()
			return HttpResponse("Registration Done")
			return render(request,'employee_home.html')

		except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'emp_complaint_form.html')


def performanceEvaluation(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			ename = request.POST.get('name')
			id = request.POST.get('id')
			dept = request.POST.get('dept')
			pname = request.POST.get('pname')
			date= request.POST.get('date')
			duty = request.POST.get('duty')
			strength = request.POST.get('strength')
			weakness =request.POST.get('weakness')
			skill_improve = request.POST.get('skills')
			evaluate_obj = PerformanceEvaluation(emp_name=ename, emp_dept=dept, date=date, project=pname,
			                    emp_duty=duty, emp_strength=strength, emp_weakness=weakness, 
								plan_to_improve=skill_improve)
			evaluate_obj.save()
			return HttpResponse("Completed")
			return render(request,'project_manger_home.html')

			
		except Exception as a:
			print(str(a))
			return HttpResponse("Failed")
	return render(request, 'emp_performance_evaluation.html')


def costEstimation(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			software = request.POST.get('software')
			hardware = request.POST.get('hardware')
			equipment = request.POST.get('equipment')
			total_cost =request.POST.get('total')
			cost_obj = CostEstimation(software_cost=software, hardware_cost=hardware, 
			            equipment_cost=equipment,total_cost=total_cost)
			cost_obj.save()
			return HttpResponse("Added")
			return render(request,'project_manger_home.html')

		except Exception as e:
			print(str(e))
			return HttpResponse("Failed To Add")
	return render(request,'cost_estimation.html')

def intimationDetails(request):
	if request.method == 'POST':
		try:
			date = request.POST.get('date')
			mail = request.POST.get('mail')
			description = request.POST.get('reason')
			intimate_obj = Intimation(mail=mail, intimation_date=date, intimation_description=description)
			intimate_obj.save()
			return HttpResponse("Intimation Sent")
		except Exception as e:
			print(str(e))
			return HttpResponse("Failed To Sent")
	return render(request, 'intimation.html')

def leaveApply(request):
	if request.method =='POST':
		try:
			leave_available = request.POST.get('available')
			leave_taken = request.POST.get('taken')
			leave_remian = request.POST.get('remain')
			leave_type = request.POST.get('leavetype')
			from_date = request.POST.get('fdate')
			to_date = request.POST.get('edate')
			days = request.POST.get('days')
			reason = request.POST.get('reason')
			file_upload = request.POST.get('') #file upload, add in settingd.py
			return HttpResponse("Appiled Successfully")
			return render(request, 'employee_home.html')
		except Exception as e:
			print(str(e))
			return HttpResponse("Failed To Sent")
			return render(request, 'leave_form.html')

def projectReg(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			title = request.POST.get('ptitle')
			sponser = request.POST.get('psponser')
			cost = request.POST.get('pcost')
			manager = request.POST.get('pmanger')
			sdate = request.POST.get('psdate')
			edate = request.POST.get('pedate')
			reg_obj = Project(project_title=title, project_sponser=sponser, project_manger=manager, 
				      project_cost=cost, project_start_date=sdate, project_end_date=edate )
			reg_obj.save()
			return HttpResponse("Registration Done")
			return render(request,'project_manager_home.html')

		except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'project_register.html')


def questionPaper(request):
	if request.method == 'POST':
		try:
			questions = request.POST.get('question')
			print(questions)
			option1= request.POST.get('option1')
			print(option1)
			option2 = request.POST.get('option2')
			print(option2)
			option3 = request.POST.get('option3')
			print(option3)
			option4 = request.POST.get('option4')
			print(option4)
			answer = request.POST.get('answer')
			question_obj = QuestionPaper(question=questions, option1=option1, option2=option2, option3=option3, option4=option4)
			question_obj.save()
			return HttpResponse("Added")
			return render(request, 'hr_home.html')
		
		except Exception as e:
			print(str(e))
			return HttpResponse("Failed To Add")
	return render(request, 'question_paper.html')



def mockTest(request):
	if request.method == 'POST':
		try:
			questions = request.POST.get('question')
			print(questions)
			option1= request.POST.get('option1')
			print(option1)
			option2 = request.POST.get('option2')
			print(option2)
			option3 = request.POST.get('option3')
			print(option3)
			option4 = request.POST.get('option4')
			print(option4)
			answer = request.POST.get('answer')
			print(answer)
			mock_obj = MockTest(mock_question=questions, option1=option1, option2=option2, option3=option3, 
			                    option4=option4, mock_answer=answer)
			mock_obj.save()
			return HttpResponse("Added")
			return render(request, 'hr_home.html')
		
		except Exception as e:
			print(str(e))
			return HttpResponse("Failed To Add")
	return render(request, 'mock_test.html')


