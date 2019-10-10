from django.urls import path
from . import views

urlpatterns =[
	path('',views.userLogin),
	path('logout',views.userLogout),
	path('register/',views.registration),
	path('hr_home',views.redirect_hr_home),
	path('project_home',views.redirect_project_home),
	path('employee_home',views.redirect_employee_home),
	path('employee_view',views.employee_view),
	path('candidate_register/',views.candidateRegistration),
	path('candidate_view/',views.candidate_view),
	path('candidate_resume/',views.candidate_resume),
	path('questionpaper/',views.addQuestion),
	path('question_view/',views.onlineExam),
	path('mocktest/',views.mockTest),
	path('mockdisplay/',views.mockDisplay),
	path('payment/',views.payment),
	# path('emp_profile/',views.empProfile),
	path('intimation/',views.intimationDetails),
	path('leaveform/', views.leaveApply),
	path('projectreg/',views.projectReg),
    path('complaintreg/',views.complaintReg),
	path('evaluation/', views.performanceEvaluation)

]