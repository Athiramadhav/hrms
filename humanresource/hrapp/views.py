from django.shortcuts import render, redirect
from django.template import Template,loader
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def userLogin(request):
	try:
		if request.method == 'POST':
			lusername = request.POST.get('username')
			lpassword = request.POST.get('password')
			user_obj=Login.objects.get(username=lusername, password=lpassword)
			emp_details= EmployeeProfile.objects.get(fk_login=user_obj.id)

			request.session['userid'] = user_obj.id
			
			if emp_details.designation=="HR Manager":
				return HttpResponseRedirect('hr_home')
			elif emp_details.designation=="Project Manager":
				return HttpResponseRedirect('project_home')
			else:
				return HttpResponseRedirect('employee_home')
			
		return render(request,'login.html')
	except Exception as e:
			print(str(e))
			return render(request,'candidate_home.html')

def redirect_hr_home(request):
	try:
		if 'userid' in request.session:
			return render(request, 'hr_home.html')
		return redirect('/hrapp/')
	except Exception as e:
		print(str(e))

# def redirect_candidate_home(request):
# 	try:
# 		if 'userid' in request.session:
# 			# cndt_obj = Candidate.objects.get(id=request.session['userid'])
# 			return render(request, 'candidate_home.html')
# 		return redirect('/hrapp/')
# 	except Exception as e:
# 		print(str(e))

def redirect_project_home(request):
	try:
		if 'userid' in request.session:
			pm_obj = EmployeeProfile.objects.get(id=request.session['userid'])
			return render(request, 'project_home.html')
		return redirect('/hrapp/')
	except Exception as e:
		print(str(e))

def redirect_employee_home(request):
	try:
		if 'userid' in request.session:
			return render(request, 'employee_home.html')
		return redirect('/hrapp/')
	except Exception as e:
		print(str(e))


def userLogout(request):
	try:
		if 'userid' in request.session:
			del request.session['userid']
		return redirect('/hrapp')
	except Exception as e:
		print(str(e))
		return redirect('/hrapp')


def registration(request):
	if request.method =='POST' and request.FILES['file_uploads']:
		try:
			vupload_image = request.FILES['file_uploads']
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
			check_user_email=Login.objects.filter(username=vemail).exists()
			if check_user_email==False:
				login_obj = Login(username=vemail, password=vpassword)
				login_obj.save()
				if login_obj.id>0:
					emp_detail = EmployeeProfile(fname=vfname,lname=vlname,gender=vgender,dob=vdob,
					address=vaddress,phone=vphone,designation=vdesignation,emp_qualification=vqualification,
					emp_experience=vexperience,salary=vsalary,join_date=vjoin_date,upload_image=vupload_image,fk_login=login_obj)
					emp_detail.save()
					if emp_detail.id>0:
						return HttpResponse('registration succecssful')
		except Exception as e:
			print(str(e))
			return HttpResponse('registration failed')
	return render(request, 'employee_registration.html')

def employee_view(request):
	user_objs = EmployeeProfile.objects.all()
	context={'userlist':user_objs}
	print(context)
	return render(request, 'employee_detail.html',context)

"""def employee_profile(request):
	emp_obj = EmployeeProfile.objects.all()
	user=[]
	context={}
	for emp_objs in user_obj:
		if emp_objs.designation=="":"""

def candidateRegistration(request):
	if request.method == 'POST' and request.FILES['resume_uploads']:
		try:
			var_candidate_name = request.POST.get('candidatename')
			var_dob = request.POST.get('dob')
			var_address = request.POST.get('address')
			var_phone_no = request.POST.get('mobileno')
			var_gender = request.POST.get('gender')
			var_qualification = request.POST.get('qualification')
			var_year_of_pass = request.POST.get('yrofpass')
			var_email = request.POST.get('email')
			var_password = request.POST.get('password')
			upload_resume = request.FILES['resume_uploads']
			var_experience = request.POST.get('experience')
			var_company = request.POST.get('company_name')
			var_designation = request.POST.get('candidate_desg')
			var_period = request.POST.get('period')
			check_candidate=Login.objects.filter(username=var_email).exists()
			if check_candidate==False:
				login_object = Login(username=var_email, password=var_password)
				login_object.save()
				if login_object.id>0:
					candidate_detail = Candidate(candidate_name=var_candidate_name,dob=var_dob,address=var_address,phone_no=var_phone_no,
				               			gender=var_gender,qualification=var_qualification,year_of_pass=var_year_of_pass,experience=var_experience,fk_login=login_object)
					candidate_detail.save()
					resume_detail = Resume(resume_upload=upload_resume,fk_candidate_id=candidate_detail)
					resume_detail.save()
					if candidate_detail.experience=='Yes':
						experience_detail = CandidateExperiance(company_name=var_company,designation=var_designation,period=var_period,
										fk_candidate_id=candidate_detail)
						experience_detail.save()
					else:
						experience_details=CandidateExperiance(company_name='NIL',designation='NIL',period=0,
										fk_candidate_id=candidate_detail)
						experience_details.save()
					if candidate_detail.id>0:
						return HttpResponse('Registerd')
		except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'login.html')

@csrf_exempt
def candidate_view(request):
	candidate_objs = Candidate.objects.all()
	context = {'candidatelist':candidate_objs}
	return render(request, 'candidate_list.html',context)

@csrf_exempt
def candidate_resume(request):
	resume_id = request.GET.get('id')
	resume_obj = Resume.objects.get(id=resume_id)
	exp_obj = CandidateExperiance.objects.get(fk_candidate_id=resume_id) 
	print(exp_obj)
	image = {'resume':resume_obj,'experience':exp_obj}
	return render(request,'candidate_resume.html',image)

@csrf_exempt
def addQuestion(request):
	if request.method=='POST':
		try:
			val_question = request.POST.get('question')
			val_option1 = request.POST.get('option1')
			val_option2 = request.POST.get('option2')
			val_option3 = request.POST.get('option3')
			val_option4 = request.POST.get('option4')
			val_ans = request.POST.get('answer')
			exam_object = QuestionPaper(question=val_question, option1=val_option1, option2=val_option2, option3=val_option3, option4=val_option4, answer=val_ans)
			exam_object.save()
			return HttpResponse('saved')
		except Exception as e:
			print(str(e))
			return HttpResponse('not saved')
	return render(request,'question_paper.html')

def onlineExam(request):
	try:
		if request.method== 'POST':
			ans_obj = request.POST.get('')
	except:
		print('error')
		
@csrf_exempt
def mockTest(request):
	if request.method == 'POST':
		try:
			questions = request.POST.get('question')
			option1= request.POST.get('option1')
			option2 = request.POST.get('option2')
			option3 = request.POST.get('option3')
			option4 = request.POST.get('option4')
			answer = request.POST.get('answer')
			mock_obj = MockTest(mock_question=questions, option1=option1, option2=option2, option3=option3, 
			                    option4=option4, mock_answer=answer)
			mock_obj.save()
			return HttpResponse("Added")
		
		except Exception as e:
			print(str(e))
			return HttpResponse("Failed To Add")
	return render(request, 'mock_test.html')

def mockDisplay(request):
	try:
		if request.method == 'POST':
			print(request.POST)
			qid = int(request.POST['ques_id'])
			print(qid)
			mock_obj = MockTest.objects.values().get(id=qid+1)
			print(mock_obj)
			mock_obj.pop('mock_answer')
			return JsonResponse({'data':mock_obj})
			
		else:
			mock_obj = MockTest.objects.get(id=1)
			return render(request,'mock_test_view.html',{'mock':mock_obj})

	except Exception as e:
		print(str(e))
		return HttpResponse("Failed to load")

# def mockDisplay(request):
# 	mock_obj = MockTest.objects.all()
# 	context = {'mocks':mock_obj}
# 	return render(request, 'mock_test_view.html',context)


def payment(request):
	try:
		if request.method == 'POST':
			desig = request.POST['designation']
			print(desig)
	# emp_objs = EmployeeProfile.objects.filter(designation=desig).exists()
	# context={'list':emp_objs}
		return render(request,'payment_slip.html')
	except Exception as e:
		print(str(e))


def complaintReg(request):
	if request.method == 'POST':
		try:
			print(request.POST)
			ename = request.POST['name']
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
	else:
		user_id = request.session['userid']
		employee_obj = EmployeeProfile.objects.get(fk_login=user_id)
		return render(request, 'emp_complaint_form.html',{'employee': employee_obj})


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
			file_upload = request.FILES['fileupload']
			leave_obj = EmployeeLeave(leave_available=leave_available, leave_taken=leave_taken,
			                          leave_remains=leave_remian, leave_type=leave_type, 
									  from_date=from_date,to_date=to_date, no_of_days=days, 
									  leave_reason=reason)
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
			print(title)
			sponser = request.POST.get('psponser')
			print(sponser)
			cost = request.POST.get('pcost')
			print(cost)
			manager = request.POST.get('pmanger')
			print(manager)
			sdate = request.POST.get('psdate')
			print(sdate)
			edate = request.POST.get('pedate')
			print(edate)
			reg_obj = Project(project_title=title, project_sponser=sponser, project_manger=manager, 
				      project_cost=cost, project_start_date=sdate, project_end_date=edate )
			reg_obj.save()
			return render(request,'project_register.html',{'response':'Registration done Successfully'})

		except Exception as e:
			print(str(e))
			return render(request,'project_register.html',{'response':'Registration Failed'})
	return render(request, 'project_register.html')















































































































			
			
#  		else:
#  			mock_obj = MockTest.objects.get(id=1)
#  			return render(request,'mock_test_view.html',{'mock':mock_obj})

#  	except Exception as e:
#  			print(str(e))
#  			return HttpResponse("Failed to load")
# else:
# 			mock_obj = MockTest.objects.get(id=1)
# 			return render(request,'mock_test_view.html',{'mock':mock_obj})

# 	except Exception as e:
# 			print(str(e))
# 			return HttpResponse("Failed to load")
















