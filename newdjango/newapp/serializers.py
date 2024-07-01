from rest_framework import serializers
from .models import TempJobSeekerProfile, Notification

class TempJobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempJobSeekerProfile
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
