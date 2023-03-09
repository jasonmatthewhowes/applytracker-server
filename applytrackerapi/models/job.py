from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=155)
    job_post_link = models.URLField(null=True, max_length=2048)
    resume = models.ForeignKey("Resume", on_delete=models.CASCADE, related_name='job_resume', null=True)
    cover_letter = models.ForeignKey("Cover_Letter", on_delete=models.CASCADE, related_name='cover_letter_jobs', null=True, )
    applied = models.DateField(null=True)
    due_date = models.DateField(null=True)
    description = models.TextField(null=True)
    job_service = models.ForeignKey("Job_Service",on_delete=models.CASCADE, related_name='job_service_jobs', null=True )
    role = models.ForeignKey("Role",on_delete=models.CASCADE, related_name='role_jobs', null=True )
    timestamp = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    companyjobs = models.ForeignKey("Company",on_delete=models.CASCADE, related_name='company_per_job', null=True )
    contact = models.ForeignKey("Contact",on_delete=models.CASCADE, related_name='job_contact', null=True )
    temperature = models.IntegerField(null=True)
