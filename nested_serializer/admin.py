from django.contrib import admin
from . models import *

# Register your models here.

class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name' ,'gender']
admin.site.register(Singer,SingerAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display=['id', 'title','duration' ,'singer']
admin.site.register(Song,SongAdmin)