from django.db import models
from .choices import *
# from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    studied = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    attendance = models.CharField(max_length=100,choices = ch)

    def __str__(self) -> str:
        return self.name
