from django.contrib import admin

from .models import Student_Study_Data, Patrol_Data

class Student_Study_DataAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'week_name')
    search_fields = ['student_name', 'week_name']

class Patrol_DataAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'date')
    search_fields = ['student_name', 'date']

admin.site.register(Student_Study_Data, Student_Study_DataAdmin)
admin.site.register(Patrol_Data, Patrol_DataAdmin)
