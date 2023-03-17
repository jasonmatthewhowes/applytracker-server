"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Cover_Letter
from applytrackerapi.models import Job
from django.contrib.auth.models import User

from rest_framework.decorators import action

class Cover_LetterView(ViewSet):
    """Level up view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized game type
        """

        cover_letter = Cover_Letter.objects.get(pk=pk)
        filteredby = request.auth.user_id
        if cover_letter.user_id == filteredby:
            serializer = Cover_LetterSerializer(cover_letter)
            return Response(serializer.data)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)



    def list(self, request):
        """Handle GET requests

        Returns:
            Response -- JSON serialized list of game types
        """
        cover_letters = Cover_Letter.objects.all()
        filteredby = request.auth.user_id
        cover_letters = cover_letters.filter(user = filteredby)
        serializer = Cover_LetterSerializer(cover_letters, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized cover_letter instance
    """
        user = User.objects.get(pk=request.auth.user_id)
        # job = Job.objects.get(pk=request.data["job"])
        cover_letter = Cover_Letter.objects.create(
            user = user,
            cover_letter_url = request.data ["cover_letter_url"],
            name = request.data["name"],
            finalized = request.data["finalized"],
            # job = job,
            body = request.data["body"]
        )
        serializer = Cover_LetterSerializer(cover_letter)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        cover_letter = Cover_Letter.objects.get(pk=pk)
        cover_letter_url = request.data ["cover_letter_url"]
        name = request.data["name"]
        finalized = request.data["finalized"]
        body = request.data["body"]
        #get the objects to pass because of foreign key
        user = User.objects.get(pk=request.auth.user_id)
        job = Job.objects.get(pk=request.data["job"])
       
        cover_letter.user = user
        cover_letter.cover_letter_url = cover_letter_url
        cover_letter.name= name
        cover_letter.finalized = finalized
        cover_letter.job = job
        cover_letter.body = body
        cover_letter.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        cover_letter = Cover_Letter.objects.get(pk=pk)
        permission = request.auth.user_id
        if cover_letter.user_id == permission:
            cover_letter.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else: 
            return Response(None, status=status.HTTP_401_UNAUTHORIZED)

    
    # @action(methods=['post'], detail=True)
    # def signup(self, request, pk):
    #     """Post request for a user to sign up for an cover_letter"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     cover_letter = Cover_Letter.objects.get(pk=pk)
    #     cover_letter.attendees.add(gamer)
    #     return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    
    # @action(methods=['delete'], detail=True)
    # def leave(self, request, pk):
    #     """Post request for a user to sign up for an cover_letter"""
    
    #     gamer = Gamer.objects.get(user=request.auth.user)
    #     cover_letter = Cover_Letter.objects.get(pk=pk)
    #     cover_letter.attendees.remove(gamer)
    #     return Response({'message': 'Gamer deleted'}, status=status.HTTP_204_NO_CONTENT)
    

class Cover_LetterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'full_name')
class Cover_LetterJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id','name','description')
 

class Cover_LetterSerializer(serializers.ModelSerializer):
    user = Cover_LetterUserSerializer(many = False )
    job = Cover_LetterJobSerializer(many = False )

    class Meta:
        model = Cover_Letter
        fields = ('id', 'user', 'cover_letter_url','name', 'finalized', 'job', 'body')
