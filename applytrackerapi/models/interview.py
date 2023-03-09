from django.db import models
from django.contrib.auth.models import User

class Interview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    location = models.CharField(null=True, max_length=400)
    job = models.ForeignKey("Job", on_delete=models.CASCADE, related_name='job_interview', null=False )
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE, related_name='interview_contact', null=True )
    