from django.contrib import admin
from .models import Attendance, StudentRegister
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'early_leave', 'late', 'absent')

class StudentRegisterAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'username', 'teacher')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(StudentRegister, StudentRegisterAdmin)