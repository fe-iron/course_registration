from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=50, null=True, default="no name")
    email = models.EmailField(max_length=30, null=False)
    subject = models.CharField(max_length=50, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(max_length=50, null=True, default="No Name")
    email = models.EmailField(max_length=50, null=False)
    dob = models.DateField()
    fname = models.CharField(max_length=50, null=True, default="No Father Name")
    mname = models.CharField(max_length=50, null=True, default="No Mother Name")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
