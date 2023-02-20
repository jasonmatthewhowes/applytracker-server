from django.db import models


class Event(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_creator_events')
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='game_events')
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    attendees = models.ManyToManyField("Gamer", through="Attendance") 

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value