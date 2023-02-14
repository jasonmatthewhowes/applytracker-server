from django.db import models


class EventAttendance(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='gamer_events')
    event = models.ForeignKey("Event", null=False, blank=False, on_delete=models.CASCADE, related_name='event_name')
    
