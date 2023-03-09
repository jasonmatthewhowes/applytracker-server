"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from applytrackerapi.models import Event
from applytrackerapi.models import Game
from applytrackerapi.models import Gamer
from applytrackerapi.models import Attendance
from rest_framework.decorators import action

class EventView(ViewSet):
    """Level up view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single
        
        Returns:
            Response -- JSON serialized game type
        """

        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
    
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        events = Event.objects.all()

        if "game" in request.query_params:
            filteredby = request.query_params['game'][0]
            events = events.filter(game=filteredby)

        # Set the `joined` property on every event
        for event in events:
        # Check to see if the gamer is in the attendees list on the event
            event.joined = event.gamer in event.attendees.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
        Response -- JSON serialized event instance
    """
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            gamer=gamer,
            game=game,
            name=request.data["name"],
            description=request.data["description"],
            date = request.data["date"],
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        #handles put request
        event = Event.objects.get(pk=pk)
        event.name = request.data["name"]
        event.description = request.data["description"]
        event.date = request.data["date"]
        #get the object to pass because of foreign key
        game = Game.objects.get(pk=request.data["game"])
        gamer = Gamer.objects.get(pk=request.data["gamer"])
        event.game = game
        event.gamer = gamer
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    
    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(gamer)
        return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    
    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """Post request for a user to sign up for an event"""
    
        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.remove(gamer)
        return Response({'message': 'Gamer deleted'}, status=status.HTTP_204_NO_CONTENT)
    
class EventGamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('user', 'bio')
 

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer 
    """
    gamer = EventGamerSerializer(many = False )

    class Meta:
        model = Event
        fields = ('id', 'game', 'gamer', 'name', 'description', 'date', 'attendees', 'joined')
