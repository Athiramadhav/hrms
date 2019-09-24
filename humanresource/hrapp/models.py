from django.db import models

# Create your models here.

class CompanyProfile(models.Model):
	company_title = models.CharField(max_length=20)
	company_estb_year = models.IntegerField()
	address = models.CharField(max_length=100)
	phone = models.IntegerField()
	fax = models.IntegerField()
	website = models.CharField(max_length=25)
	email = models.CharField(max_length=25)


class Permission(models.Model):
	fk_role_id = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
	permission_title = models.CharField(max_length=20)


class EmployeeProfile(models.Model):
	upload_image= models.FileField(upload_to ='pictures/')
	fname = models.CharField(max_length=25)
	lname = models.CharField(max_length=25)
	gender = models.CharField(max_length=25)
	dob = models.DateField(max_length=25)
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	password = models.CharField(max_length=15)
	designation = models.CharField(max_length=15)
	emp_qualification = models.CharField(max_length=25)
	emp_experience = models.CharField(max_length=25)
	salary = models.CharField(max_length=25)
	join_date = models.CharField(max_length=25)


class Login(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	fk_role_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)


class Candidate(models.Model):
	candidate_name = models.CharField(max_length=20)
	dob = models.DateField(max_length=20)
	address = models.CharField(max_length=50)
	phone_no = models.IntegerField()
	gender = models.CharField(max_length=15)
	qualification = models.CharField(max_length=15)
	year_of_pass = models.IntegerField()
	experience = models.CharField(max_length=10)
	email = models.CharField(max_length=20)
	password = models.CharField(max_length=15)


class Resume(models.Model):
	resume= models.FileField(upload_to ='file/')
	fk_candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class CandidateExperiance(models.Model):
	company_name = models.CharField(max_length=20)
	designation = models.CharField(max_length=15)
	period = models.IntegerField()
	fk_candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	fk_resume_id = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Interview(models.Model):
	interview_type = models.CharField(max_length=20)
	interview_Date = models.DateField()
	interview_time = models.TimeField()
	interview_location = models.CharField(max_length=20)
	fk_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class CallLetter(models.Model):
	fk_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	post = models.CharField(max_length=20)
	join_date = models.DateField()
	join_time = models.TimeField()


class QuestionPaper(models.Model):
	question = models.CharField(max_length=50)
	option1 = models.CharField(max_length=20)
	option2 = models.CharField(max_length=20)
	option3 = models.CharField(max_length=20)
	option4 = models.CharField(max_length=20)
	answer = models.CharField(max_length=20)


class MockTest(models.Model):
	mock_question = models.CharField(max_length=50)
	option1 = models.CharField(max_length=20)
	option2 = models.CharField(max_length=20)
	option3 = models.CharField(max_length=20)
	option4 = models.CharField(max_length=20)
	mock_answer = models.CharField(max_length=20)


class ExamDetail(models.Model):
	exam_startdate = models.DateField()
	exam_enddate = models.DateField()
	exam_starttime = models.TimeField()
	exam_endtime= models.TimeField()
	exam_duration = models.TimeField()


class Mail(models.Model):
	from_address = models.CharField(max_length=20)
	to_address = models.CharField(max_length=20)
	content = models.CharField(max_length=100)
	attachment = models.FileField(upload_to ='')


class Result(models.Model):
	fk_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	mark = models.IntegerField()
	rank = models.CharField(max_length=10)

	
class Attendance(models.Model):
	date = models.DateField(max_length=25)
	time = models.DateField(max_length=25)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class ComplaintReg(models.Model):
	e_name = models.CharField(max_length=25)
	e_desgination = models.CharField(max_length=25)
	e_dept = models.CharField(max_length=25)
	e_addr = models.CharField(max_length=25)
	e_phone = models.IntegerField()
	c_name = models.CharField(max_length=25)
	complaint_desg = models.CharField(max_length=25)
	complaint_dept = models.CharField(max_length=25)
	compaint_description = models.CharField(max_length=60)
	date_of_incident = models.DateField(max_length=25)
	time_of_incident = models.DateField(max_length=25)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)


class Intimation(models.Model):
	emp_name = models.CharField(max_length=25) 
	date = models.DateField(max_length=25)
	mail = models.CharField(max_length=25)
	dept = models.CharField(max_length=25)
	reason = models.CharField(max_length=50)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class EmployeeLeave(models.Model):
	emp_name = models.CharField(max_length=50)
	dept = models.CharField(max_length=50)
	leave_available = models.IntegerField()
	leave_taken = models.IntegerField()
	leave_remains = models.IntegerField()
	leave_type = models.CharField(max_length=50)
	from_date = models.DateField(max_length=50)
	to_date = models.DateField(max_length=50)
	no_of_days = models.IntegerField()
	leave_reason = models.CharField(max_length=50)
 	
class ProjectRegister(models.Model):
	project_title = models.CharField(max_length=50)
	project_sponser = models.CharField(max_length=50)
	project_manger = models.CharField(max_length=25)
	project_cost = models.IntegerField()
	project_start_date = models.DateField(max_length=25)
	project_end_date = models.DateField(max_length=25)
	project_expense = models.IntegerField(max_length=25)


class Resource(models.Model):
	hardware_req = models.CharField(max_length=50)
	software_req = models.CharField(max_length=50)
	equipment_req = models.CharField(max_length=50)


class ResourceAllocate(models.Model):
	project_title = models.CharField(max_length=25)
	dept = models.CharField(max_length=25)
	task_title = models.CharField(max_length=25)
	resource_type = models.CharField(max_length=25)
	resource_available = models.CharField(max_length=25)
	resource_allocated = models.CharField(max_length=25)


class CompanyProfile(models.Model):
	company_title = models.CharField(max_length=20)
	company_estb_year = models.IntegerField()
	address = models.CharField(max_length=100)
	phone = models.IntegerField()
	fax = models.IntegerField()
	website = models.CharField(max_length=25)
	email = models.CharField(max_length=25)

	
class TaskAdd(models.Model):
    fk_project_id  = models.IntegerField(ProjectRegister, max_length=25)
    task_title = models.CharField(max_length=50)
    task_priority = models.CharField(max_length=25)
    task_start_date = models.DateField(max_length=25)
    task_end_date = models.DateField(max_length=25)
    team_lead = models.CharField(max_length=50)
	

class CostEstimation(models.Model):
	software_cost = models.IntegerField()
	hardware_cost = models.IntegerField()
	equipment_cost = models.IntegerField()
	total_cost = models.IntegerField()


class TaskAssign(models.Model):
	team_lead = models.CharField(max_length=25)
	reminder = models.DateField(max_length=25)
	fk_task_id = models.IntegerField(max_length=25)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class Intimation(models.Model):
	to_address = models.CharField(max_length=50)
	intimation_date = models.DateField(max_length=25)
	intimation_description = models.CharField(max_length=60)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class Vacany(models.Model):
	no_of_vacanies = models.IntegerField(max_length=25)
	dept_name = models.CharField(max_length=25)
	post = models.CharField(max_length=25)
	emp_qualification = models.CharField(max_length=25)
	emp_experience = models.CharField(max_length=25)
	time_period = models.DateField(max_length=25)


class PerformanceEvaluation(models.Model):
	emp_name = models.CharField(max_length=25)
	emp_dept = models.CharField(max_length=25)
	date = models.DateField(max_length=25)
	project = models.CharField(max_length=25)
	emp_duty = models.CharField(max_length=100)
	emp_strength = models.CharField(max_length=75)
	emp_weakness = models.CharField(max_length=75)
	plan_to_improve = models.CharField(max_length=75)
	fk_project_id = models.ForeignKey(ProjectRegister, on_delete=models.CASCADE)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)