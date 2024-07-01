from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification, TempJobSeekerProfile
from .serializers import TempJobSeekerProfileSerializer, NotificationSerializer

@api_view(['POST'])
def jobseeker_signup(request):
    serializer = TempJobSeekerProfileSerializer(data=request.data)
    if serializer.is_valid():
        # Save the temporary job seeker profile
        serializer.save()
        
        # Create notification for admin
        Notification.objects.create(
            name=request.data.get('name'),
            email=request.data.get('email'),
            action='Job seeker signed up',
            notification_type='signup'
        )
        
        return Response({'message': 'Please wait for admin approval'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_notifications(request):
    notifications = Notification.objects.all()
    print(notifications)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
def approve_job_seeker(request, profile_id):
    temp_profile = get_object_or_404(TempJobSeekerProfile, id=profile_id)
    # Optionally, move data to JobSeekerProfile model and delete temp profile
    temp_profile.delete()  # Delete temporary profile after approval
    # Create notification for admin
    Notification.objects.create(
        name=temp_profile.name,
        email=temp_profile.email,
        action='Job seeker approved',
        notification_type='approval'
    )
    return Response({'message': 'Job seeker approved'})

@api_view(['POST'])
def reject_job_seeker(request, profile_id):
    temp_profile = get_object_or_404(TempJobSeekerProfile, id=profile_id)
    temp_profile.delete()  # Delete temporary profile after rejection
    # Create notification for admin
    Notification.objects.create(
        name=temp_profile.name,
        email=temp_profile.email,
        action='Job seeker rejected',
        notification_type='rejection'
    )
    return Response({'message': 'Job seeker rejected'})
