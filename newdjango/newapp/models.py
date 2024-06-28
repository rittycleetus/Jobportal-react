
from django.db import models





class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    dob = models.DateField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    educational_info = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    blocked = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True,blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='employer_logos/')
    website = models.URLField()
    address = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128,blank=True, null=True)  
    blocked = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

