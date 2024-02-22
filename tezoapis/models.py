from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    empid = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOB = models.DateField()
    emailid = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=15)
    joining = models.DateField()
    location = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    AssignManager = models.CharField(max_length=100, blank=True)
    AssignProject = models.CharField(max_length=100, blank=True)
    profilepath = models.CharField(max_length=255)
    status = models.CharField(max_length=50)