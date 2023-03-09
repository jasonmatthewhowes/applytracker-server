from django.db import models


class Company(models.Model):
    name = models.CharField(null=False, max_length=155)
    job = models.ManyToManyField("Job")
