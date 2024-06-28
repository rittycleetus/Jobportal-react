from rest_framework import serializers
from .models import JobSeekerProfile

class JobseekerSerialisers(serializers.ModelSerializer):
    class Meta:
        model : JobSeekerProfile
        fields = '__all__'