from django.urls import path
from . import views

urlpatterns =[
	path('userlogin/',views.userLogin),
	path('register/',views.registration),
	path('candidateregister/', views.candidateRegistration),
	path('exam/', views.questionPaper),
	path('mocktest/', views.mockTest),
	path('projectreg/',views.projectReg),
    # path('complaintreg/',views.complaintReg)

	# path('registeremployee/',views.)
	# path('exam/',)
]