"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Role
from applytrackerapi.models import Job
from django.contrib.auth.models import User

from rest_framework.decorators import action

class RoleView(ViewSet):
    """ApplyTracker View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized role
        """

        role = Role.objects.get(pk=pk)
        # filteredby = request.auth.user_id
        # if role.user_id == filteredby:
        serializer = RoleSerializer(role)
        return Response(serializer.data)
        # else: 
        #     return Response(None, status=status.HTTP_401_UNAUTHORIZED)



    def list(self, request):
        """Handle GET requests

        Returns:
            Response -- JSON serialized list of game types
        """
        roles = Role.objects.all()
        # filteredby = request.auth.user_id
        # roles = roles.filter(user = filteredby)
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized role instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        role = Role.objects.create(
            user = user,
            name = request.data["name"],
            
            
        )
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        role = Role.objects.get(pk=pk)
        name = request.data ["name"]
        
        #get the objects to pass because of foreign key
    
        job = Job.objects.get(pk=request.data["job"])
        user = User.objects.get(pk=request.auth.user_id)
        role.user = user
        role.name = name
        role.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        role = Role.objects.get(pk=pk)
        permission = request.auth.user_id
        if role.user_id == permission:
            role.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    
class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'name')
