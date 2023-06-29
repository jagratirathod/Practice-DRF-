from django.db import models
from . managers import CustomManager , CustomManagerAdv

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    roll = models.IntegerField()

    objects = models.Manager()
    student = CustomManager()
    stud = CustomManagerAdv()

