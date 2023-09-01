from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100 , null=False)
    lname = models.CharField(max_length=120, blank=True)
    phone = models.IntegerField()
    date = models.DateField()
    address = models.CharField(max_length=120 , default="Indore madhyapradesh")
