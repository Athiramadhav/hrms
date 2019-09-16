from django.db import models

# Create your models here.

class Login(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	role = models.CharField(max_length=20)

"""class EmployeeRegistration(models.Models):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	gender = models.CharField(max_length=20)
	dob = models.DateField(max_length=20)"""

class CandidateRegistration(models.Model):
	candidate_name = models.CharField(max_length=20)
	dob = models.DateField(max_length=20)
	address = models.CharField(max_length=50)
	gender = models.CharField(max_length=15)
	qualification = models.CharField(max_length=15)
	year_of_pass = models.IntegerField()
	resume = models.FileField(upload_to =)
	experiance = model.CharField(max_length=10)
	email = models.CharField(max_length=20)
	resume= models.FileField(upload_to ='file/')
	password = models.CharField(max_length=15)

class CandidateExperiance(models.Model):
	company_name = models.CharField(max_length=20)
	designation = models.CharField(max_length=15)
	period = models.IntegerField()

class Interview(model.Model):
	interview_type = models.CharField(max_length=20)
	interview_Date = models.DateField()
	interview_time = models.IntegerField()
	interview_location = models.CharField(max_length=20)
	fk_candidate = models.
	
class Mail(models.Model):
	fromaddr

class HRregistration(models.Model):
	hr_fname = models.CharField(max_length=25)
	hr_lname = models.CharField(max_length=25)
	hr_gender = models.CharField(max_length=25)
	hr_dob = models.DateField(max_length=25)
	hr_address = models.CharField(max_length=50)
	hr_phone = models.CharField(max_length=25)
	hr_email = models.CharField(max_length=25)
	hr_password = models.CharField(max_length=15)
	hr_designation = models.CharField(max_length=15)
	hr_qualification = models.CharField(max_length=25)
	hr_experience = models.CharField(max_length=25)
	hr_salary = models.CharField(max_length=25)
	hr_join_date = models.CharField(max_length=25)

class Result(models.Model):

class Filter(models.Model):


class Company(models.Model):
	company_title = models.CharField(max_length=20)


# class Role(models.Model):
# 	role_title = models.CharField(max_length=15)
# 	fk_company_id = models.ForiegnKey(Company, on_delete=models.CASCADE)
		
	
class EmployeeProfile(models.Model):
	upImage= models.FileField(upload_to ='pictures/')
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


class Project(models.Model):
	project_title = models.CharField(max_length=50)
	project_name = models.CharField(max_length=50)
	project_sponser = models.CharField(max_length=50)
	project_manger = models.CharField(max_length=25)
	team_lead = models.CharField(max_length=50)
	team_members = models.IntegerField(max_length=25)
	project_start_date = models.DateField(max_length=25)
	project_end_date = models.DateField(max_length=25)
	project_expense = models.IntegerField(max_length=25)
	fk_resource_id = models.ForiegnKey(Resource, on_delete=models.CASCADE)
	fk_employee_id = models.ForigenKey(EmployeeProfile, on_delete=models.CASCADE)


class Resource(models.Model):
	hardware_req = models.CharField(max_length=50)
	software_req = models.CharField(max_length=50)
	eployess_req = models.CharField(max_length=50)
	expense = models.IntegerField(max_length=25)
	fk_project_id = models.ForiegnKey(Project, on_delete=models.CASCADE)


class ProjectTaskAssign(models.Model):
	task_title = models.CharField(max_length=50)
	task_assignee = models.CharField(max_length=30)
	task_status =
	task_priority = models.CharField(max_length=25)
	task_start_date = models.DateField(max_length=25)
	task_end_date = models.DateField(max_length=25)
	percent_complete = models.IntegerField(max_length=25)
	task_comment = models.CharField(max_length=50)
	task_fixed_cost = models.IntegerField(max_length=25)
	task_estimated_cost = models.IntegerField(max_length=25)
	task_actual_hours = models.DateField(max_length=25)

class ComplaintReg(models.Model):
	c_name = models.CharField(max_length=25)
	complaint_title = models.CharField(max_length=25)
	complaint_dept = models.CharField(max_length=25)
	compaint_description = models.CharField(max_length=60)
	date_of_incident = models.DateField(max_length=25)
	time_of_incident = models.DateField(max_length=25)
	fk_employee_id = models.ForigenKey(EmployeeProfile, on_delete=models.CASCADE)

class EmployeeLeave(models.Model):
	leave_date_from = models.DateField(max_length=25)
	leave_date_to = models.DateField(max_length=25)
	no_leaves = models.IntegerField(max_length=25)
	approved_leave = models.IntegerField(max_length=25)
	leave_reason = models.DateField(max_length=25)
	fk_employee_id = models.ForigenKey(EmployeeProfile, on_delete=models.CASCADE)

class PerformanceEvaluation(models.Model):
	perform_description = models.CharField(max_length=100)
	epmloyee_strength = models.CharField(max_length=75)
	epmloyee_weakness = models.CharField(max_length=75)
	plan_to_improve = models.CharField(max_length=75)
	fk_project_id = models.ForiegnKey(Project, on_delete=models.CASCADE)
	fk_employee_id = models.ForigenKey(EmployeeProfile, on_delete=models.CASCADE)

class CostEstimation(models.Model):
	software_cost = models.IntegerField(max_length=60)
	hardware_cost = models.IntegerField(max_length=60)
	infrastructure_cost = models.IntegerField(max_length=60)
	implementaion_cost = models.IntegerField(max_length=60)
	total_cost = models.IntegerField(max_length=60)


class TaskReminder(models.Model):
	task_reminder_end_date = models.DateField(max_length=25)
	fk_task_id = models.IntegerField(max_length=25)
	fk_employee_id = models.ForigenKey(EmployeeProfile, on_delete=models.CASCADE)

class Intimation(models.Model):
	to_address = models.CharField(max_length=50)
	intimation_date = models.DateField(max_length=25)
	intimation_description = models.CharField(max_length=60)
	fk_employee_id = models.ForiegnKey(EmployeeProfile, on_delete=models.CASCADE)
