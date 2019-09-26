from django.urls import path
from . import views

urlpatterns =[
	path('',views.userLogin),
	path('home',views.home),
	path('register/',views.registration),
	path('registeremployee',views.home),
	path('intimation/',views.intimationDetails)
	#path('exam/',views.addQuestio
	path('candidateregister/', views.candidateRegistration),
	path('exam/', views.questionPaper),
	path('mocktest/', views.mockTest),
	path('projectreg/',views.projectReg),
    # path('complaintreg/',views.complaintReg)

	# path('registeremployee/',views.)
	# path('exam/',)
]