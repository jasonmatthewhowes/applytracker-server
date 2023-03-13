from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=155)
    