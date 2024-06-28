from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import JobSeekerProfile
from .serializers import JobseekerSerialisers

@api_view(['GET'])
def ok(request):
    users = JobSeekerProfile.objects.all()
    serializers = JobseekerSerialisers(users, many=True)
    print("Fetching Job Seeker Profiles...")
    return Response(serializers.data)