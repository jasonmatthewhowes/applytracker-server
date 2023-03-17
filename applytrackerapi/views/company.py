"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Company
from django.contrib.auth.models import User

from rest_framework.decorators import action

class CompanyView(ViewSet):
    """ApplyTracker View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized company
        """

        company = Company.objects.get(pk=pk)
        # filteredby = request.auth.user_id
        # if company.user_id == filteredby:
        serializer = CompanySerializer(company)
        return Response(serializer.data)
        # else: 
        #     return Response(None, status=status.HTTP_401_UNAUTHORIZED)



    def list(self, request):
        """Handle GET requests

        Returns:
            Response -- JSON serialized list
        """
        companies = Company.objects.all()
        # filteredby = request.auth.user_id
        # companies = companies.filter(user = filteredby)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized company instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        company = Company.objects.create(
            user = user,
            name = request.data["name"],
            
            
        )
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        company = Company.objects.get(pk=pk)
        name = request.data ["name"]
        
        #get the objects to pass because of foreign key

        user = User.objects.get(pk=request.auth.user_id)
        company.user = user
        company.name = name
        company.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        company = Company.objects.get(pk=pk)
        permission = request.auth.user_id
        if company.user_id == permission:
            company.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name')
