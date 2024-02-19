from django.contrib import admin
from . models import *

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name']
admin.site.register(Person,PersonAdmin)
