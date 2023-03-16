from django.db import models
from django.contrib.auth.models import User

class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    location = models.CharField(null=True, max_length=400)
    job = models.ForeignKey("Job", on_delete=models.CASCADE, related_name='job_interview', null=False )
    interviewcontacts = models.ManyToManyField("Contact", through="InterviewAttendance") 

    @property
    def joining(self):
        return self.__joining

    @joining.setter
    def joining(self, value):
        self.__joining = value