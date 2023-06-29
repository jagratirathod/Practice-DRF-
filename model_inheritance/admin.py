from django.contrib import admin
from . models import *

# Abstract model inheritance -

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'fees','name','age']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'salary','name','age']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment','name','age','date']


# multi-table inheritance -

class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname' , 'city']
admin.site.register(ExamCenter, ExamCenterAdmin)

class Student_info_Admin(admin.ModelAdmin):
    list_display = ['id', 'name' , 'roll','cname','city']
admin.site.register(Student_info, Student_info_Admin)

# Proxy model inheritance -

@admin.register(ExamsCenters)
class ExamsCentersAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname' , 'city']


@admin.register(MyExamsCenters)
class MyExamsCentersAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname' , 'city']
