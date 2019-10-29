from django.db import models

# Create your models here.

class CompanyProfile(models.Model):
	company_title     = models.CharField(max_length=20)
	company_estb_year = models.IntegerField()
	address           = models.CharField(max_length=100)
	phone             = models.IntegerField()
	fax               = models.IntegerField()
	website           = models.CharField(max_length=25)
	email             = models.CharField(max_length=25)


class Permission(models.Model):
	fk_role_id       = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
	permission_title = models.CharField(max_length=20)

class Login(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

class EmployeeProfile(models.Model):
	fname             = models.CharField(max_length=25)
	lname             = models.CharField(max_length=25)
	gender            = models.CharField(max_length=25)
	dob               = models.DateField(max_length=25)
	address           = models.CharField(max_length=50)
	phone             = models.CharField(max_length=25)
	designation       = models.CharField(max_length=15)
	emp_qualification = models.CharField(max_length=25)
	emp_experience    = models.CharField(max_length=25)
	salary            = models.CharField(max_length=25)
	join_date         = models.CharField(max_length=25)
	upload_image      = models.FileField(upload_to ='pictures/')
	fk_login          = models.ForeignKey(Login, on_delete=models.CASCADE)




class Candidate(models.Model):
	candidate_name = models.CharField(max_length=20)
	dob            = models.DateField(max_length=20)
	address        = models.CharField(max_length=50)
	phone_no       = models.IntegerField()
	gender         = models.CharField(max_length=15)
	qualification  = models.CharField(max_length=15)
	year_of_pass   = models.IntegerField()
	experience     = models.CharField(max_length=10)
	email          = models.CharField(max_length=20)
	password       = models.CharField(max_length=15)


class Resume(models.Model):
	resume          = models.FileField(upload_to ='file/')
	fk_candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class CandidateExperiance(models.Model):
	company_name    = models.CharField(max_length=20)
	designation     = models.CharField(max_length=15)
	period          = models.IntegerField()
	fk_candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	fk_resume_id    = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Interview(models.Model):
	interview_type     = models.CharField(max_length=20)
	interview_Date     = models.DateField()
	interview_time     = models.TimeField()
	interview_location = models.CharField(max_length=20)
	fk_candidate       = models.ForeignKey(Candidate, on_delete=models.CASCADE)


class CallLetter(models.Model):
	fk_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	post         = models.CharField(max_length=20)
	join_date    = models.DateField()
	join_time    = models.TimeField()


class QuestionPaper(models.Model):
	question = models.CharField(max_length=50)
	option1  = models.CharField(max_length=20)
	option2  = models.CharField(max_length=20)
	option3  = models.CharField(max_length=20)
	option4  = models.CharField(max_length=20)
	answer   = models.CharField(max_length=20)


class MockTest(models.Model):
	mock_question = models.CharField(max_length=50)
	option1       = models.CharField(max_length=20)
	option2       = models.CharField(max_length=20)
	option3       = models.CharField(max_length=20)
	option4       = models.CharField(max_length=20)
	mock_answer   = models.CharField(max_length=20)



class ExamDetail(models.Model):
	exam_startdate = models.DateField()
	exam_enddate   = models.DateField()
	exam_starttime = models.TimeField()
	exam_endtime   = models.TimeField()
	exam_duration  = models.TimeField()


class Mail(models.Model):
	from_address = models.CharField(max_length=20)
	to_address   = models.CharField(max_length=20)
	content      = models.CharField(max_length=100)
	attachment   = models.FileField(upload_to ='attachment/')


class Result(models.Model):
	fk_candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	fk_question  = models.ForeignKey(MockTest, on_delete=models.CASCADE,default=None)
	mark         = models.IntegerField()

	
class Location(models.Model):
	location = models.CharField(max_length=25)

class Dept(models.Model):
	dept_name = models.CharField(max_length=50)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, default='None')


class ProjectAllocation(models.Model):
	category        = models.CharField(max_length=50)
	team_lead       = models.CharField(max_length=50)
	fk_employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, default='None')


class Project(models.Model):
	project_title      = models.CharField(max_length=50)
	project_sponser    = models.CharField(max_length=50)
	project_manger     = models.CharField(max_length=25)
	project_cost       = models.IntegerField()
	project_start_date = models.DateField()
	project_end_date   = models.DateField()
	project_team_lead  = models.ForeignKey(ProjectAllocation, on_delete=models.CASCADE)


class Complaint(models.Model):
	e_name               = models.CharField(max_length=25)
	e_desgination        = models.CharField(max_length=25)
	e_dept               = models.CharField(max_length=25)
	e_addr               = models.CharField(max_length=25)
	e_phone              = models.IntegerField()
	c_name               = models.CharField(max_length=25)
	complaint_desg       = models.CharField(max_length=25)
	complaint_dept       = models.CharField(max_length=25)
	compaint_description = models.CharField(max_length=60)
	date_of_incident     = models.DateField()
	time_of_incident     = models.TimeField()
	fk_employee_id       = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)


class EmployeeLeave(models.Model):
	leave_available = models.IntegerField()
	leave_taken     = models.IntegerField()
	leave_remains   = models.IntegerField()
	leave_type      = models.CharField(max_length=50)
	from_date       = models.DateField(max_length=50)
	to_date         = models.DateField(max_length=50)
	no_of_days      = models.IntegerField()
	leave_reason    = models.CharField(max_length=50)
	fk_employee_id  = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
 	

class Resource(models.Model):
	hardware_req  = models.CharField(max_length=50)
	software_req  = models.CharField(max_length=50)
	equipment_req = models.CharField(max_length=50)


class ResourceAllocate(models.Model):
	project_title      = models.CharField(max_length=25)
	dept               = models.CharField(max_length=25)
	task_title         = models.CharField(max_length=25)
	resource_type      = models.CharField(max_length=25)
	resource_available = models.CharField(max_length=25)
	resource_allocated = models.CharField(max_length=25)
	fk_resource_id     = models.ForeignKey(Resource, on_delete=models.CASCADE)
	fk_project_id      = models.ForeignKey(Project, on_delete=models.CASCADE)
	
	
	
class TaskAdd(models.Model):
	fk_project_id   = models.ForeignKey(Project, on_delete=models.CASCADE)
	task_title      = models.CharField(max_length=50)
	task_priority   = models.CharField(max_length=25)
	task_start_date = models.DateField()
	task_end_date   = models.DateField()
	fk_team_id      = models.ForeignKey(ProjectAllocation, on_delete=models.CASCADE,default='None')
	
class CostEstimation(models.Model):
	software_cost  = models.IntegerField()
	hardware_cost  = models.IntegerField()
	equipment_cost = models.IntegerField()
	total_cost     = models.IntegerField()


class Intimation(models.Model):
	dept                   = models.CharField(max_length=50)
	mail                   = models.CharField(max_length=50)
	intimation_date        = models.DateField()
	intimation_description = models.CharField(max_length=60)
	fk_employee_id         = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)

class Vacany(models.Model):
	no_of_vacanies    = models.IntegerField()
	dept_name         = models.CharField(max_length=25)
	post              = models.CharField(max_length=25)
	emp_qualification = models.CharField(max_length=25)
	emp_experience    = models.CharField(max_length=25)
	time_period       = models.DateField()

class PerformanceEvaluation(models.Model):
	emp_name        = models.CharField(max_length=25)
	emp_dept        = models.CharField(max_length=25)
	date            = models.DateField(max_length=25)
	project         = models.CharField(max_length=25)
	emp_duty        = models.CharField(max_length=100)
	emp_strength    = models.CharField(max_length=75)
	emp_weakness    = models.CharField(max_length=75)
	plan_to_improve = models.CharField(max_length=75)
	fk_project_id   = models.ForeignKey(Project, on_delete=models.CASCADE)
	fk_employee_id  = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
