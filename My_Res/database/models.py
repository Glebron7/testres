from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    responsibilities = models.CharField(max_length=100)
    free_time = models.IntegerField()