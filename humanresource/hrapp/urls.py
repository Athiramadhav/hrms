from django.urls import path
from . import views

urlpatterns =[
	path('',views.userLogin),
	path('home',views.home),
	path('register/',views.registration),
	path('registeremployee',views.home),
	path('intimation/',views.intimationDetails),
<<<<<<< HEAD
	#path('exam/',views.addQuestio
=======
	path('exam/',views.addQuestion),
>>>>>>> 64da5aecb0f50b8d58cd6f845d33430d16196906
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