"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Interview
from applytrackerapi.models import Job
from applytrackerapi.models import Contact
from django.contrib.auth.models import User

from rest_framework.decorators import action

class InterviewView(ViewSet):
    

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized 
        """

        interview = Interview.objects.get(pk=pk)
        filteredby = request.auth.user_id
        if interview.user_id == filteredby:
            serializer = InterviewSerializer(interview)
            return Response(serializer.data)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)



    def list(self, request):
        """Handle GET requests

        Returns:
            Response -- JSON serialized list 
        """
        interviews = Interview.objects.all()
        filteredby = request.auth.user_id
        interviews = interviews.filter(user = filteredby)
        serializer = InterviewSerializer(interviews, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized interview instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        job = Job.objects.get(pk=request.data["job"])
        interview = Interview.objects.create(
            user = user,
            date = request.data["date"],
            time = request.data["time"],
            location = request.data["location"],
            job = job
        )
        serializer = InterviewSerializer(interview)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        interview = Interview.objects.get(pk=pk)
        date= request.data["date"]
        time = request.data["time"]
        location = request.data["location"]
        #get the objects to pass because of foreign key
        user = User.objects.get(pk=request.auth.user_id)
        job = Job.objects.get(pk=request.data["job"])
       
        interview.user = user
        interview.date = date
        interview.time = time
        interview.location = location
        interview.job = job
        interview.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        interview = Interview.objects.get(pk=pk)
        permission = request.auth.user_id
        if interview.user_id == permission:
            interview.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    @action(methods=['post'], detail=True)
    def connect(self, request, pk):
        """Post request for a user to connect a contact to an interview"""
    
        contact = Contact.objects.get(pk=request.data["contact"])
        interview = Interview.objects.get(pk=pk)
        interview.interviewcontacts.add(contact)
        return Response({'message': 'Contact added'}, status=status.HTTP_201_CREATED)
    
    
    @action(methods=['delete'], detail=True)
    def disconnect(self, request, pk):
        """Post request for a user to disconnect a contact from an interview"""
    
        contact = Contact.objects.get(pk=request.data["contact"])
        interview = Interview.objects.get(pk=pk)
        interview.interviewcontacts.remove(contact)
        return Response({'message': 'Contact Removed'}, status=status.HTTP_204_NO_CONTENT)
    
   


class InterviewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'full_name')
class InterviewJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','name')
class InterviewContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','full_name')
 

class InterviewSerializer(serializers.ModelSerializer):
    user = InterviewUserSerializer(many = False )
    job = InterviewJobSerializer(many = False )
    interviewcontacts = InterviewContactsSerializer(many = True )

    class Meta:
        model = Interview
        fields = ('id', 'user', 'date','time', 'location', 'job', 'interviewcontacts', 'joining')
