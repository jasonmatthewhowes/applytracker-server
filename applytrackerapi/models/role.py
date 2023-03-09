from django.db import models


class Role(models.Model):
    name = models.CharField(null=False, max_length=155)
    