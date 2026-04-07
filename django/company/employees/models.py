from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    salary = models.IntegerField()
    full_time = models.BooleanField()

    def __str__(self):
        return self.name