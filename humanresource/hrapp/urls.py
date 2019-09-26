from django.urls import path
from . import views

urlpatterns =[
	path('',views.userLogin),
	path('home',views.home),
	path('register/',views.registration),
	path('registeremployee',views.home),
	path('intimation/',views.intimationDetails)
	#path('exam/',views.addQuestion)
]