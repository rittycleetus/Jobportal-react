# serializers.py

from rest_framework import serializers
from .models import JobSeekerProfile

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerProfile
        fields = ('name', 'dob', 'username', 'profile_picture', 'educational_info', 'address')
