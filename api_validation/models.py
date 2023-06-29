from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name



    
class Entrys(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name