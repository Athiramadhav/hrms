from django.shortcuts import render,redirect
from django.template import Template, loader
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
# Create your views here.

def userLogin(request):
	try:
		if request.method == 'POST':
			lusername = request.POST.get('username')
			lpassword = request.POST.get('password')
			user_obj=Login.objects.get(username=lusername, password=lpassword)
			request.session['userid'] = user_obj.id
			emp_details= EmployeeProfile.objects.get(fk_login=user_obj.id)
			if emp_details.designation=="HR Manager":
				return HttpResponseRedirect('hr_home')
			elif emp_details.designation == "Project Manager":
				return HttpResponseRedirect('project_manager_home')
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

def redirect_employee_home(request):
	try:
		if 'userid' in request.session:
			return render(request, 'employee_home.html')
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

# 
def redirect_project_manager_home(request):
	try:
		if 'userid' in request.session:
			return render(request, 'project_manager_home.html')
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
						subject = ' REGISTRATION NOTIFICATION'
						message = 'WELCOME '+vfname+' '+vlname+' TO THE COMPANY. YOU ARE SUCCESSFULLY REGISTERED AS OUR '+vdesignation+' WITH USERNAME:'+vemail+' password: '+vpassword+'.'
						print(message)
						email_from = settings.EMAIL_HOST_USER
						recipient_list = [''+vemail+'']
						print(recipient_list)
						send_mail( subject, message, email_from, recipient_list )
						# return HttpResponse('registration succecssful')
		except Exception as e:
			print(str(e))
			return HttpResponse('registration failed')
	return render(request, 'employee_registration.html')

def employee_view(request):
	user_objs = EmployeeProfile.objects.all()
	context={'userlist':user_objs}
	return render(request, 'employee_detail.html',context)

def employee_profile(request):
	try:
		user_id = request.session['userid']
		emp_obj = EmployeeProfile.objects.get(fk_login_id=user_id)
		context={'user':emp_obj}
		if emp_obj.designation == 'HR Manager':
			return render(request, 'hr_profile.html', context)
		elif emp_obj.designation == 'Project Manager':
			return render(request, 'pm_profile.html', context)
		else:
			return render(request, 'emp_profile.html', context)
	except Exception as e:
		print(str(e))
		return HttpResponse("failed")

def edit(request):
	try:
		emp_id = request.session['userid']
		emp_object = EmployeeProfile.objects.get(fk_login_id=emp_id)
		if request.method=='POST':
			EmployeeProfile.objects.filter(id=emp_object.id).update(address=request.POST['emp_address'],phone=request.POST['emp_mobileno'],
				emp_qualification=request.POST['emp_qualification'],emp_experience=request.POST['emp_experience'],salary=request.POST['emp_salary'])
		context={'user':emp_object}
		if emp_object.designation == 'HR Manager':
			return render(request, 'hr_edit.html', context)
		elif emp_object.designation == 'Project Manager':
			return render(request, 'pm_edit.html', context)
		else:
			return render(request, 'emp_edit.html',context)
	except Exception as e:
		print(str(e))
		return HttpResponse('failed')
		
@csrf_exempt
def delete(request):
	try:
		user_id=request.GET.get('id')
		print(user_id)
		EmployeeProfile.objects.get(id=user_id).delete()
		return HttpResponse('employee deleted')
	except Exception as e:
		print(str(e))
		return HttpResponse('error')

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
			var_company1 = request.POST.get('company_name1')
			var_company2 = request.POST.get('company_name2')
			var_company3 = request.POST.get('company_name3')
			var_designation1 = request.POST.get('candidate_desg1')
			var_designation2 = request.POST.get('candidate_desg2')
			var_designation3 = request.POST.get('candidate_desg3')
			var_period1 = request.POST.get('period1')
			var_period2 = request.POST.get('period2')
			var_period3 = request.POST.get('period3')
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
						experience_detail = CandidateExperiance(company_name1=var_company1,company_name2=var_company2,company_name3=var_company3,
											designation1=var_designation1,designation2=var_designation2,designation3=var_designation3,
											period1=var_period1,period2=var_period2,period3=var_period3,fk_candidate_id=candidate_detail,fk_resume_id=resume_detail)
						experience_detail.save()
					else:
						experience_details=CandidateExperiance(company_name1='NIL',company_name2='NIL',company_name3='NIL',
											designation1='NIL',designation2='NIL',designation3='NIL',
											period1='NIL',period2='NIL',period3='NIL',fk_candidate_id=candidate_detail,fk_resume_id=resume_detail)
						experience_details.save()
					# if candidate_detail.id>0:
					# 	return HttpResponse('Registerd')
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
	image = {'resume':resume_obj,'experience':exp_obj}
	return render(request,'candidate_resume.html',image)

@csrf_exempt
def addQuestion(request):
	if request.method == 'POST':
		try:
			val_questions = request.POST.get('question')
			print(val_questions)
			val_option1= request.POST.get('option1')
			print(val_option1)
			val_option2 = request.POST.get('option2')
			print(val_option2)
			val_option3 = request.POST.get('option3')
			print(val_option3)
			val_option4 = request.POST.get('option4')
			print(val_option4)
			val_answer = request.POST.get('answer')
			print(val_answer)
			exam_object = QuestionPaper(question=val_questions, option1=val_option1, option2=val_option2, option3=val_option3,
						 option4=val_option4, answer=val_answer)
			exam_object.save()
			return HttpResponse('saved')
		except Exception as e:
			print(str(e))
			return HttpResponse('not saved')
	return render(request,'question_paper.html')

def onlineExam(request):
	try:
		if request.method == 'POST':
			candidate_id = int(request.session['userid'])
			qid = int(request.POST['ques_id'])
			online_obj = QuestionPaper.objects.values().get(id=qid+1)
			online_obj.pop('answer')
			request.session['current_question'] = online_obj['id']
			return JsonResponse({'data':online_obj})
		else:
			qid = None
			# qid = request.session.get('current_question')
			if qid:
				online_obj = QuestionPaper.objects.values().get(id=qid)
			else:
				online_obj = QuestionPaper.objects.values().get(id=20)	
			return render(request,'qp_view.html',{'online':online_obj})
	except Exception as e:
		print(str(e))
		return HttpResponse("Failed to load")

		
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
 			qid = int(request.POST['ques_id'])
 			mock_obj = MockTest.objects.values().get(id=qid+1)
 			mock_obj.pop('mock_answer')
 			return JsonResponse({'data':mock_obj})

 		else:
 			mock_obj = MockTest.objects.get(id=1)
 			return render(request,'mock_test_view.html',{'mock':mock_obj})

 	except Exception as e:
 		print(str(e))
 		return HttpResponse("Failed to load")

@csrf_exempt
def payment(request):
	try:
		if request.method == 'POST':
			desi = request.POST.get('desig')
			print(desi)
			print("**************")
			emp_objs=EmployeeProfile.objects.filter(designation=desi)
			json_data = list(emp_objs.values())
			return JsonResponse(json_data,safe=False)
	
	except Exception as e:
		print(str(e))
		return HttpResponse('failed')
	return render(request,'payment_slip.html')

@csrf_exempt
def interview(request):
	try:
		if request.method =='POST':
			intvw_type = request.POST.get('interview_type')
			print(intvw_type)
			intrvw_dt = request.POST.get('interview_dt')
			intrvw_time = request.POST.get('interview_time')
			lctn = request.POST.get('location')
			intrvw_obj = Interview(interview_type=intvw_type,interview_Date=intrvw_dt,interview_time=intrvw_time,interview_location=lctn)
			intrvw_obj.save()
			subject = ' REGISTRATION NOTIFICATION'
			message = ' You have cleared the online examination and is selected for the technical interview scheduled at '+lctn+ ' on '+intrvw_dt+ 'for further details vist our website.' 
			print(message)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [''+vemail+'']
			print(recipient_list)
			send_mail( subject, message, email_from, recipient_list )
			return HttpResponse('Registerd')
	except Exception as e:
		print(str(e))
		return HttpResponse("Failed")
	return render(request, 'interview_detail.html')

@csrf_exempt
def exam_detail(request):
	try:
		if request.method =='POST':
			strt_dt = request.POST.get('start_dt')
			strt_tym = request.POST.get('start_time')
			ed_dt = request.POST.get('end_dt')
			ed_tym = request.POST.get('end_time')
			drtn = request.POST.get('duration')
			exam_obj = ExamDetail(exam_startdate =strt_dt,exam_enddate=ed_dt,exam_starttime =strt_tym,exam_endtime=ed_tym,exam_duration=drtn)
			# exam_obj.save()
			subject = ' ONLINE EXAM NOTIFICATION'
			message = ' Exam notification is available in the site'
			email_from = settings.EMAIL_HOST_USER
			print(email_from)
			# recipient = Candidate.objects.all().filter(fk_login.username__in)
			# print(recipient)
			recipient_list = ['theerthakp95@gmail.com']
			send_mail( subject, message, email_from, recipient_list )
			# return HttpResponse('success')
	except Exception as e:
		print(str(e))
	return render(request, 'exam_details.html')

@csrf_exempt
def intimationDetails(request):
	try:
		if request.method == 'POST':
			date = request.POST.get('mail_date')
			mail = request.POST.get('email')
			description = request.POST.get('reason')
			intimate_obj = Intimation(mail=mail, intimation_date=date, intimation_description=description)
			# intimate_obj.save()
			subject = ' INTIMATION MAIL'
			message = ''+description+''
			print(message)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [''+mail+'']
			print(recipient_list)
			send_mail( subject, message, email_from, recipient_list )
			return HttpResponse("Intimation Sent")
	except Exception as e:
			print(str(e))
			return HttpResponse("Failed To Sent")
	return render(request, 'intimation.html')

@csrf_exempt
def leaveType(request):
	try:
		if request.method =='POST':
			var_type = request.POST.get('type')
			print(var_type)
			var_day = request.POST.get('days')
			print(var_day)
			var_status = request.POST.get('status')
			print(var_status)
			leave_typ_obj = LeaveType(leave_type =var_type,no_of_days =var_day,status=var_status)
			print(leave_typ_obj)
			leave_typ_obj.save()
			# return HttpResponse('success')
	except Exception as e:
		print(str(e))
	return render(request, 'leave_type.html')

def leaveAdd(request):
	try:
		leave_typ_obj=LeaveType.object.all()
		print(leave_typ_obj)
		# if request.method =='POST':
	except Exception as e:
		print(str(e))
		
def leaveReport(request):
	return render(request, 'leave_report_view.html')

def complaintReport(request):
	try:

		complaint_obj = Complaint.objects.all()
		context = {'complaintlist':complaint_obj}
		return render(request, 'complaint_view.html', context)

	except Exception as e:
		print(str(e))
	
@csrf_exempt
def callLetter(request):
	try:
		if request.method == 'POST':
			val_post = request.POST.get('post')
			val_jn_dt = request.POST.get('join_date')
			val_jn_tym = request.POST.get('join_time')
			call_obj = CallLetter(post=val_post,join_date=val_jn_dt,join_time=val_jn_tym)
			call_obj.save()
	except Exception as e:
		print(str(e))
	return render(request, 'callletter.html')


def complaintReg(request):
	if request.method == 'POST':
		try:
			name = request.session['userid']
			emp_obj  = EmployeeProfile.objects.get(id=name)
			print(name)
			cact =request.POST.get('act')
			date = request.POST.get('date')
			time = request.POST.get('time')
			comp_reg = Complaint(compaint_description=cact, date_of_incident=date, time_of_incident=time,fk_employee_id=emp_obj)
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
	try:
		empname = EmployeeProfile.objects.filter(designation='Other')
		print(empname)
		emp_id = EmployeeProfile.objects.filter(id__in=empname)
		print(emp_id)

		if request.method == 'POST':
			print(request.POST)
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

		else:
		 emp_obj = EmployeeProfile.objects.all()
		 return render(request, 'emp_performance_evaluation.html',{'employee' : emp_obj})
		
		
	except Exception as a:
		print(str(a))
		return HttpResponse("Failed")

	


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
				      project_cost=cost, project_start_date=sdate, project_end_date=edate)
			reg_obj.save()
			if reg_obj.id > 0:
				context={}
				context['currentproject']= reg_obj
				print(context)
				return render(request,'project_register.html', context)
		except Exception as e:
			print(str(e))
			return render(request,'project_register.html',{'response':'Registration Failed'})
	return render(request, 'project_register.html')


def taskAdd(request):
	try:
		if request.method == 'POST':
			pro_id = request.GET.get('id')
			project_obj = Project.objects.get(id=pro_id)
			task = request.POST.get('task')
			print(task)
			priority = request.POST.get('priority')
			print(priority)
			sdate = request.POST.get('sdate')
			print(sdate)
			edate = request.POST.get('edate')
			print(edate)
			name = request.POST.get('team_lead')
			print(name)
			team = ProjectAllocation.objects.get(team_lead=name)
			print(team)
			task_add_obj = TaskAdd(fk_project_id=project_obj,task_title=task, task_priority=priority, task_start_date=sdate,
			                         task_end_date=edate, fk_team_id=team)
			task_add_obj.save()

		else:
			try:
				project_obj = Project.objects.get(id=request.GET.get('id'))
			except:
				project_obj = {}
			team_lead_obj = ProjectAllocation.objects.all()
			context = {}
			context["projectlist"]= project_obj
			context["teamlist"]= team_lead_obj
			return render(request,'task_add.html',context)
	except Exception as e:
			print(str(e))
			return render(request,'task_add.html',{'response':'Failed'})
	return render(request, 'task_add.html')

@csrf_exempt
def task_view(request):
	task_obj = TaskAdd.objects.all()
	context = {'tasks':task_obj}
	return render(request, 'task_view.html',context)



def assign(request):
	try:
		if request.method == 'POST':
			print(request.POST)
			category = request.POST['selection']
			print(category)
			teamlead = request.POST['tlead']
			print(teamlead)
			name = request.POST.getlist('employeecheckbox')
			count = 0
			login = Login.objects.filter(username__in=name)
			print(login)
			for obj in login:
				assign_obj = ProjectAllocation(category=category, team_lead=teamlead,fk_login=obj)
				assign_obj.save()
				if assign_obj.id > 0:
					count += 1
			if count == len(name):
				return HttpResponse('Success done')
			else:
				return HttpResponse('Failed')


		else:
			empname = EmployeeProfile.objects.filter(designation='Other').values('fk_login')
			print(empname)
			if empname != "":
				employee = Login.objects.only('username').filter(id__in=empname)
				print(employee)
				response_obj = {'username':employee}
				return render(request, 'assign.html',response_obj)
			
	except Exception as e:
			print(str(e))
			return render(request,'assign.html',{'response':'Failed'})
	return render(request, 'assign.html')

		
def vaccancy(request):
	try:
		if request.method == 'POST':
			post = request.POST['post']
			print(post)
			vacancy = request.POST['vacancy']
			print(vacancy)
			qualification = request.POST['qualify']
			print(qualification)
			exp = request.POST['exp']
			print(exp)
			time = request.POST['time']
			print(time)
			vacancy_obj = Vacany(no_of_vacanies=vacancy,post=post, emp_qualification=qualification, 
			                       emp_experience=exp, time_period=time)
			vacancy_obj.save()
			return HttpResponse("Success")
	except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'vacancy.html')


def roster_view(request):
	# if emp_name = EmployeeProfile.objects.filter(designation='Other'):

	roster_obj = TaskAdd.objects.all()
	context = {'rosterlist':roster_obj}
	return render(request, 'roster.html',context)

def vacancy_view(request):
	vacancy_obj = Vacany.objects.all()
	context = {'list': vacancy_obj}
	print(context)
	return render(request, 'report_vacancy.html',context)


def dept(request):
	try:
		if request.method == 'POST':
			id = EmployeeProfile.objects.only(id)
			print(id)
			dept = request.POST['dept']
			print(dept)
			dept_obj = Dept(dept_name=dept, fk_employee_id=id)
			dept_obj.save()
			return render("Added")
			return render(request,'employee_home.html')
		else:
			user_id = request.session['userid']
			employee_obj = EmployeeProfile.objects.get(fk_login=user_id)
			return render(request, 'dept.html',{'employee': employee_obj})
	except Exception as e:
		print(str(e))
		return HttpResponse("Failed")
	

def company(request):
	try:
		if request.method == 'POST':
			title = request.POST['title']
			print(title)
			year = request.POST['year']
			print(year)
			address = request.POST['address']
			print(address)
			phone = request.POST['phone']
			print(phone)
			fax = request.POST['fax']
			print(fax)
			website = request.POST['site']
			print(website)
			email = request.POST['mail']
			print(email)
			company_obj = CompanyProfile(company_title=title, company_estb_year=year, address=address, phone=phone,fax=fax, website=website, email=email)
			company_obj.save()
			return HttpResponse("Success")

		else:
			return render(request, 'company.html')

	except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'company.html')


def company_view(request):
	company_obj = CompanyProfile.objects.all()
	context = {'companylist':company_obj}
	return render(request, 'company_profile.html',context)


def project_view(request):
	project_obj = Project.objects.all()
	context = {'projectlist':project_obj}
	return render(request, 'report_project.html',context)

def task_view(request):
	task_obj = TaskAdd.objects.all()
	context = {'tasks':task_obj}
	return render(request, 'task_view.html',context)

def resource(request):
	try:
		if request.method == 'POST':
			resource = request.POST['resource']
			print(resource)
			types = request.POST['types']
			print(types)
			resource_obj = Resource(resource=resource, types=types)
			print("helloooooo")
			resource_obj.save()
			return HttpResponse("Success")
		else:
			return render(request, 'resource_add.html')
			
	except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'resource_add.html')


def notification(request):
	try:
		if request.method == 'POST':
			team_lead_obj = Login.objects.get(username=request.POST['email'])
			print(team_lead_obj.username)
			email_from = settings.EMAIL_HOST_USER
			message = 'Your are assigned to the following project'
			recipient_list=[team_lead_obj.username]
			print(recipient_list)
			send_mail('Hello',message,email_from,recipient_list)
			
except Exception as e:
			print(str(e))
			return HttpResponse("Failed")
	return render(request, 'taskadd.html')

