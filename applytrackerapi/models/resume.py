from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume_url = models.URLField(null=True, max_length=300)
    resume_name = models.CharField(null=False, max_length=155)
    date_reviewed = models.DateField(null=True)
    body = models.TextField(null=True)
    role = models.ForeignKey("Role", on_delete=models.CASCADE, null=True)

