
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JobSeeker, TempJobSeekerProfile,TempEmployerProfile,Employer1,CustomUser,JobSeekerProfile
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
        Employer1.objects.create(
            company_name=request.data.get('company_name'),
            email=request.data.get('email'),
            is_approved=False,
          
        )
        
        return Response({'message': 'Employer profile created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_new_employer_requests(request):
    new_requests = Employer1.objects.all
    print(f"Number of new employer requests: {new_requests.count()}")  
    serializer = EmployerSerializer(new_requests, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def approve_job_seeker_request(request, id):
    try:
        # Get the TempJobSeekerProfile instance to approve
        temp_profile = TempJobSeekerProfile.objects.get(id=id)
        
        # Create or update JobSeeker profile
        user_data = {
            'username': temp_profile.username,
            'email': temp_profile.email,
            'password': temp_profile.password,
        }
        user, created = CustomUser.objects.update_or_create(email=temp_profile.email, defaults=user_data)

        job_seeker_data = {
            'name': temp_profile.name,
            'email': temp_profile.email,
            'is_approved': True,
        }
        job_seeker, created = JobSeeker.objects.update_or_create(email=temp_profile.email, defaults=job_seeker_data)

        job_seeker_profile_data = {
            'user': user,
            'name': temp_profile.name,
            'dob': temp_profile.dob,
            'username': temp_profile.username,
            'profile_picture': temp_profile.profile_picture,
            'educational_info': temp_profile.educational_info,
            'address': temp_profile.address,
        }
        job_seeker_profile, created = JobSeekerProfile.objects.update_or_create(user=user, defaults=job_seeker_profile_data)

        # Delete TempJobSeekerProfile instance
        temp_profile.delete()

        # Return success response
        return Response({"message": "Job seeker approved successfully."})

    except TempJobSeekerProfile.DoesNotExist:
        return Response({"error": "TempJobSeekerProfile not found."}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)