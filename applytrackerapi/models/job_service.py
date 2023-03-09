from django.db import models


class Job_Service(models.Model):
    name = models.CharField(null=False, max_length=155)
    