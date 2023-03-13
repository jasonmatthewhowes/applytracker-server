from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=False, max_length=155)
    last_name = models.CharField(null=False, max_length=155)
    email = models.CharField(null=True, max_length=155)
    linkedin_url = models.CharField(null=True, max_length=155)
    title = models.CharField(null=True, max_length=155)
    phone = models.CharField(null=True, max_length=155)
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name='contact_company', null=True )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'