

from rest_framework import serializers
from .models import JobSeeker, TempJobSeekerProfile,TempEmployerProfile,Employer1

class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'

class TempJobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempJobSeekerProfile
        fields = '__all__'

class TempEmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempEmployerProfile
        fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer1
        fields = '__all__'