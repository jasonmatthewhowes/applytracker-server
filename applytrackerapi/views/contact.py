"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Contact
from applytrackerapi.models import Company
from django.contrib.auth.models import User

from rest_framework.decorators import action

class ContactView(ViewSet):
    """ApplyTracker View"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized contact
        """

        contact = Contact.objects.get(pk=pk)
        filteredby = request.auth.user_id
        if contact.user_id == filteredby:
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)



    def list(self, request):
        """Handle GET requests

        Returns:
            Response -- JSON serialized list of game types
        """
        contacts = Contact.objects.all()
        filteredby = request.auth.user_id
        contacts = contacts.filter(user = filteredby)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized contact instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        company = Company.objects.get(pk=request.data["company"])
        contact = Contact.objects.create(
            user = user,
            first_name = request.data["first_name"],
            last_name = request.data["last_name"],
            email = request.data["email"],
            linkedin_url = request.data["linkedin_url"],
            title = request.data["title"],
            phone = request.data["phone"],
            company = company
            
        )
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        contact = Contact.objects.get(pk=pk)
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        linkedin_url = request.data["linkedin_url"]
        title = request.data["title"]
        phone = request.data["phone"]
        
        #get the objects to pass because of foreign key
    
        user = User.objects.get(pk=request.auth.user_id)
        company = Company.objects.get(pk=request.data["company"])
        contact.user = user
        contact.first_name = first_name
        contact.last_name = last_name
        contact.email = email
        contact.linkedin_url = linkedin_url
        contact.title = title
        contact.phone = phone
        contact.company= company
        contact.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        permission = request.auth.user_id
        if contact.user_id == permission:
            contact.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)
class CompanyContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name')
    
class ContactSerializer(serializers.ModelSerializer):
    company = CompanyContactsSerializer(many = False)
    class Meta:
        model = Contact
        fields = ('id', 'full_name','first_name', 'last_name', 'email', 'linkedin_url', 'title', 'phone', 'company')
