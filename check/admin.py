from django.contrib import admin
from .models import Attendance, StudentRegister, PatrolCheck
class StudentRegisterAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'username', 'teacher')
    search_fields = ['student', 'username']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'early_leave', 'late', 'absent')
    search_fields = ['date', 'user']

class PatrolCheckAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    search_fields = ['user']

admin.site.register(StudentRegister, StudentRegisterAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(PatrolCheck, PatrolCheckAdmin)