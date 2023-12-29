from django.contrib import admin

from .models import Student_Study_Data, Patrol_Data, Patrol_Weekly_Data, Total_Weekly_Study_Data, Average_Study_Data

class Student_Study_DataAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'week_name')
    search_fields = ['student_name', 'week_name']

class Patrol_DataAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'date')
    search_fields = ['student_name', 'date']

class Patrol_Weekly_DataAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'week_name')
    search_fields = ['student_name', 'week_name']

class Total_Weekly_Study_DataAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'week_name', 'week_start_date', 'week_end_date')
    search_fields = ['student_name', 'week_name']

class Average_Study_DataAdmin(admin.ModelAdmin):
    list_display = ('week_name',)
    search_fields = ['week_name']

admin.site.register(Student_Study_Data, Student_Study_DataAdmin)
admin.site.register(Patrol_Data, Patrol_DataAdmin)
admin.site.register(Patrol_Weekly_Data, Patrol_Weekly_DataAdmin)
admin.site.register(Total_Weekly_Study_Data, Total_Weekly_Study_DataAdmin)
admin.site.register(Average_Study_Data, Average_Study_DataAdmin)