from django.urls import path
from . import views

urlpatterns =[
	path('',views.userLogin),
	path('register/',views.registration),
	#path('registeremployee',views.home)
	#path('exam/',views.addQuestion)
]