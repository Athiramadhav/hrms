from django.urls import path
from . import views

urlpatterns =[
<<<<<<< HEAD
	path('',views.userLogin),
	path('home',views.home),
	path('register/',views.registration),
	path('registeremployee',views.home),
	path('intimation/',views.intimationDetails)
	#path('exam/',views.addQuestion)
=======
	path('userlogin/',views.userLogin),
	path('register/',views.registration),
	path('candidateregister/', views.candidateRegistration),
	path('exam/', views.questionPaper),
	path('mocktest/', views.mockTest),
	path('projectreg/',views.projectReg),
    # path('complaintreg/',views.complaintReg)

	# path('registeremployee/',views.)
	# path('exam/',)
>>>>>>> 77b519a7e2c6cc427a42e373d7894abd1f7872b7
]