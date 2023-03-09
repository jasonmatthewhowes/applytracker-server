from django.db import models
from django.contrib.auth.models import User

class Cover_Letter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_letter_url = models.URLField(null=True, max_length=300)
    name = models.CharField(null=False, max_length=155)
    finalized = models.BooleanField(null=True)
    job = models.ForeignKey("Job", on_delete=models.CASCADE, related_name='job_cover_letter', null=True )
    body = models.CharField(null=True, max_length=10000)
    