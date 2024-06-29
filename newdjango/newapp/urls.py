# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jobseeker_signup/', views.JobSeekerSignupView, name='jobseeker_signup'),
    path('userlogin/', views.userlogin, name='userlogin'),
]
