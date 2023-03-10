"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Resume
from applytrackerapi.models import Role
from django.contrib.auth.models import User

from rest_framework.decorators import action

class ResumeView(ViewSet):
    """Level up view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized game type
        """

        resume = Resume.objects.get(pk=pk)
        filteredby = request.auth.user_id
        if resume.user_id == filteredby:
            serializer = ResumeSerializer(resume)
            return Response(serializer.data)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)



    def list(self, request):
        """Handle GET requests

        Returns:
            Response -- JSON serialized list of game types
        """
        resumes = Resume.objects.all()
        filteredby = request.auth.user_id
        resumes = resumes.filter(user = filteredby)
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized resume instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        role = Role.objects.get(pk=request.data["role"])
        resume = Resume.objects.create(
            user = user,
            resume_url = request.data ["resume_url"],
            resume_name = request.data["resume_name"],
            date_reviewed = request.data["date_reviewed"],
            body = request.data["body"],
            role = role
        )
        serializer = ResumeSerializer(resume)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        resume = Resume.objects.get(pk=pk)
        resume_url = request.data ["resume_url"]
        resume_name = request.data["resume_name"]
        date_reviewed = request.data["date_reviewed"]
        body = request.data["body"]
        #get the objects to pass because of foreign key
        user = User.objects.get(pk=request.auth.user_id)
        role = Role.objects.get(pk=request.data["role"])
       
        resume.user = user
        resume.resume_url = resume_url
        resume.resume_name= resume_name
        resume.date_reviewed = date_reviewed
        resume.body = body
        resume.role = role
        resume.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        resume = Resume.objects.get(pk=pk)
        permission = request.auth.user_id
        if resume.user_id == permission:
            resume.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    
    # @action(methods=['post'], detail=True)
    # def signup(self, request, pk):
    #     """Post request for a user to sign up for an resume"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     resume = Resume.objects.get(pk=pk)
    #     resume.attendees.add(gamer)
    #     return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    
    # @action(methods=['delete'], detail=True)
    # def leave(self, request, pk):
    #     """Post request for a user to sign up for an resume"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     resume = Resume.objects.get(pk=pk)
    #     resume.attendees.remove(gamer)
    #     return Response({'message': 'Gamer deleted'}, status=status.HTTP_204_NO_CONTENT)
    

class ResumeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'full_name')
class ResumeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','name')
 

class ResumeSerializer(serializers.ModelSerializer):
    user = ResumeUserSerializer(many = False )
    role = ResumeRoleSerializer(many = False )

    class Meta:
        model = Resume
        fields = ('id', 'user', 'resume_url','resume_name', 'date_reviewed', 'body', 'role')
