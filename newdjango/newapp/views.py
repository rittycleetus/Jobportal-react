
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JobSeeker, TempJobSeekerProfile,TempEmployerProfile,Employer
from .serializers import JobSeekerSerializer, TempJobSeekerProfileSerializer,TempEmployerProfileSerializer,EmployerSerializer
from rest_framework import status

@api_view(['POST'])
def jobseeker_signup(request):
    serializer = TempJobSeekerProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save the temporary job seeker profile
        
        # Create notification for admin
        JobSeeker.objects.create(
            name=request.data.get('name'),
            email=request.data.get('email'),
            is_approved=False
            
        )
        
        return Response({'message': 'Please wait for admin approval'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_new_job_seeker_requests(request):
    new_requests = JobSeeker.objects.filter(is_approved=False)
    serializer = JobSeekerSerializer(new_requests, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def employer_signup(request):
    serializer = TempEmployerProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        # Create notification for admin
        Employer.objects.create(
            name=request.data.get('name'),
            email=request.data.get('email'),
            is_approved=False,
            action='Employer signed up',
            notification_type='signup'
        )
        
        return Response({'message': 'Employer profile created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_new_employer_requests(request):
    new_requests1 = Employer.objects.filter(is_approved=False)
    serializer = EmployerSerializer(new_requests1, many=True)
    return Response(serializer.data)

