"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Job_Service
from applytrackerapi.models import Job
from django.contrib.auth.models import User

from rest_framework.decorators import action

class Job_ServiceView(ViewSet):
    """Level up view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized game type
        """

        job_service = Job_Service.objects.get(pk=pk)
        filteredby = request.auth.user_id
        if job_service.user_id == filteredby:
            serializer = Job_ServiceSerializer(job_service)
            return Response(serializer.data)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)



    def list(self, request):
        """Handle GET requests

        Returns:
            Response -- JSON serialized list of game types
        """
        job_services = Job_Service.objects.all()
        filteredby = request.auth.user_id
        job_services = job_services.filter(user = filteredby)
        serializer = Job_ServiceSerializer(job_services, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized job_service instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        job_service = Job_Service.objects.create(
            user = user,
            name = request.data["name"]
        )
        serializer = Job_ServiceSerializer(job_service)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        job_service = Job_Service.objects.get(pk=pk)
        
        name = request.data["name"]
        
        #get the objects to pass because of foreign key
        user = User.objects.get(pk=request.auth.user_id)
       
        job_service.user = user
        job_service.name= name
        job_service.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        job_service = Job_Service.objects.get(pk=pk)
        permission = request.auth.user_id
        if job_service.user_id == permission:
            job_service.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    
    # @action(methods=['post'], detail=True)
    # def signup(self, request, pk):
    #     """Post request for a user to sign up for an job_service"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     job_service = Job_Service.objects.get(pk=pk)
    #     job_service.attendees.add(gamer)
    #     return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    
    # @action(methods=['delete'], detail=True)
    # def leave(self, request, pk):
    #     """Post request for a user to sign up for an job_service"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     job_service = Job_Service.objects.get(pk=pk)
    #     job_service.attendees.remove(gamer)
    #     return Response({'message': 'Gamer deleted'}, status=status.HTTP_204_NO_CONTENT)
    

class Job_ServiceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'full_name')


class Job_ServiceSerializer(serializers.ModelSerializer):
    user = Job_ServiceUserSerializer(many = False )
 

    class Meta:
        model = Job_Service
        fields = ('id', 'user','name')
