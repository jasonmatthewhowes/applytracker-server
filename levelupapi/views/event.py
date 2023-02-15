"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models import Game
from levelupapi.models import Gamer


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

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer 
    """
    class Meta:
        model = Event
        fields = ('id', 'gamer', 'game', 'name', 'description', 'date')
