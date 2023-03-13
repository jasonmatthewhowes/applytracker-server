"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Job
from applytrackerapi.models import Resume
from applytrackerapi.models import Cover_Letter
from applytrackerapi.models import Contact
from applytrackerapi.models import Job_Service
from applytrackerapi.models import Role
from applytrackerapi.models import Company
from applytrackerapi.models import Contact
from django.contrib.auth.models import User

from rest_framework.decorators import action

class JobView(ViewSet):
    """Level up view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized job if job does not belong to user, unauthorized
        """

        job = Job.objects.get(pk=pk)
        filteredby = request.auth.user_id
        if job.user_id == filteredby:
            serializer = JobSerializer(job)
            return Response(serializer.data)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types filtered by user
        """
        jobs = Job.objects.all()
        filteredby = request.auth.user_id
        jobs = jobs.filter(user = filteredby)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized job instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        resume = Resume.objects.get(pk=request.data["resume"])
        cover_letter = Cover_Letter.objects.get(pk=request.data["cover_letter"])
        job_service = Job_Service.objects.get(pk=request.data["job_service"])
        role = Role.objects.get(pk=request.data["role"])
        companyjobs = Company.objects.get(pk=request.data["companyjobs"])
        contact = Contact.objects.get(pk=request.data["contact"])

        job = Job.objects.create(
            name = request.data["name"],
            job_post_link = request.data ["job_post_link"],
            applied = request.data ["applied"],
            description = request.data["description"],
            due_date = request.data["due_date"],
            user = user,
            resume = resume,
            cover_letter = cover_letter,
            job_service = job_service,
            role = role,
            companyjobs = companyjobs,
            contact = contact,
        )
        serializer = JobSerializer(job)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        job = Job.objects.get(pk=pk)
        job.name = request.data["name"]
        job.job_post_link = request.data ["job_post_link"]
        job.applied = request.data ["applied"]
        job.description = request.data["description"]
        job.due_date = request.data["due_date"]
        #get the objects to pass because of foreign key
        user = User.objects.get(pk=request.auth.user_id)
        resume = Resume.objects.get(pk=request.data["resume"])
        cover_letter = Cover_Letter.objects.get(pk=request.data["cover_letter"])
        job_service = Job_Service.objects.get(pk=request.data["job_service"])
        role = Role.objects.get(pk=request.data["role"])
        companyjobs = Company.objects.get(pk=request.data["companyjobs"])
        contact = Contact.objects.get(pk=request.data["contact"])
        job.user = user
        job.resume = resume
        job.cover_letter = cover_letter
        job.job_service = job_service
        job.role = role
        job.companyjobs = companyjobs
        job.contact = contact
        job.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        job = Job.objects.get(pk=pk)
        permission = request.auth.user_id
        if job.user_id == permission:
            job.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)


    
    # @action(methods=['post'], detail=True)
    # def signup(self, request, pk):
    #     """Post request for a user to sign up for an job"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     job = Job.objects.get(pk=pk)
    #     job.attendees.add(gamer)
    #     return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    
    # @action(methods=['delete'], detail=True)
    # def leave(self, request, pk):
    #     """Post request for a user to sign up for an job"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     job = Job.objects.get(pk=pk)
    #     job.attendees.remove(gamer)
    #     return Response({'message': 'Gamer deleted'}, status=status.HTTP_204_NO_CONTENT)
    
class JobResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id','resume_name', 'resume_url')
class JobCoverLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover_Letter
        fields = ('id','name', 'cover_letter_url','finalized')
class JobContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'full_name', 'email')
class JobCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')
class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')
class JobServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Service
        fields = ('id', 'name')
 

class JobSerializer(serializers.ModelSerializer):
    resume = JobResumeSerializer(many = False )
    cover_letter = JobCoverLetterSerializer(many = False )
    contact = JobContactSerializer(many = False )
    companyjobs = JobCompanySerializer(many = False )
    role = JobRoleSerializer(many = False )
    job_service = JobServiceSerializer(many = False )
    class Meta:
        model = Job
        fields = ('id', 'user', 'name', 'job_post_link', 'resume', 'cover_letter', 'applied', 'due_date', 'description', 'job_service','role', 'timestamp', 'companyjobs', 'contact', 'temperature')
