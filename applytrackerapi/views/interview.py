from django.db import models


class Interview(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='user_interview')
    job = models.ManyToManyField("Job")
    address = models.CharField(max_length=155)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    contact_attendees = models.ManyToManyField("Contact", through="InterviewAttendance") 

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value