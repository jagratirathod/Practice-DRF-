from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE , related_name = 'profile')
    otp = models.CharField(max_length = 50)
    uid = models.UUIDField(default = uuid.uuid4)
    phone_number = models.CharField(max_length = 10,unique=True)

    def __str__(self):
        return self.phone_number
