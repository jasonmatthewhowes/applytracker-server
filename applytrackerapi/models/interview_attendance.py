from django.db import models


class InterviewAttendance(models.Model):
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE, related_name='contact_interviews')
    interview = models.ForeignKey("Interview", null=False, blank=False, on_delete=models.CASCADE, related_name='interview_name')
    
