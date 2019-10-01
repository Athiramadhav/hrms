from django.urls import path
from . import views

urlpatterns =[
	path('',views.userLogin),
	path('home',views.home),
	path('register/',views.registration),
	path('registeremployee',views.home),
	path('intimation/',views.intimationDetails),
	path('exam/',views.addQuestion),
	path('candidateregister/', views.candidateRegistration),
	path('exam/', views.questionPaper),
	path('leaveform/', views.leaveApply),
	path('mocktest/', views.mockTest),
	path('mockdisplay/', views.mockDisplay),
	path('projectreg/',views.projectReg),
    path('complaintreg/',views.complaintReg)

	# path('registeremployee/',views.)
	# path('exam/',)
]