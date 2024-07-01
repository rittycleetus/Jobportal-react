# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('jobseeker_signup/', views.jobseeker_signup, name='jobseeker_signup'),
    path('get_notifications/', views.get_notifications, name='get_notifications'),
    path('jobseeker/approve/<int:profile_id>/', views.approve_job_seeker, name='approve_job_seeker'),
    path('jobseeker/reject/<int:profile_id>/', views.reject_job_seeker, name='reject_job_seeker'),
]