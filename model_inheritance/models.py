from django.db import models


# Abstract model inheritance  -

class CommanInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        abstract = True

class Student(CommanInfo):
    fees = models.IntegerField()
    date = None


class Teacher(CommanInfo):
    salary = models.IntegerField()

class Contractor(CommanInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()


# Multi - table inheritance -

class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)


class Student_info(ExamCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()


# Proxy Model -

class ExamsCenters(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

    # class Meta:
    #     ordering = ['id']


class MyExamsCenters(ExamsCenters):
    class Meta:
        proxy = True
        ordering = ['id']





