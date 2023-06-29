from django.contrib import admin
from . models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','name','tagline']
admin.site.register(Blog,BlogAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display=['id' , 'name' , 'email', 'city' , 'phone']
admin.site.register(Author,AuthorAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display=['id','name','city']
admin.site.register(Entrys,EntryAdmin)