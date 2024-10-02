from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=15)
    std = models.CharField(max_length=10)