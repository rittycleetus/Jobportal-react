# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jobseeker_signup/', views.jobseeker_signup, name='jobseeker_signup'),
    path('get_new_job_seeker_requests', views.get_new_job_seeker_requests, name='get_new_job_seeker_requests'),
    path('employer_signup/', views.employer_signup, name='employer_signup'),
    path('get_new_employer_requests',views.get_new_employer_requests,name='get_new_employer_requests'),


]