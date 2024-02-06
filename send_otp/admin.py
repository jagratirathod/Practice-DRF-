from django.contrib import admin
from . models import *

# # Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id","user","otp","uid","phone_number")
    