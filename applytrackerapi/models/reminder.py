from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE, related_name='reminder_job', null=False, )
    follow_up_date = models.DateField(null=True)
    