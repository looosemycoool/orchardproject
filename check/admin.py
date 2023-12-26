from django.contrib import admin
from .models import Break_Time_Table, BreakUser, Attendance, StudentRegister

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'class_name', 'is_teacher', 'is_student', 'is_manager')

class Break_Time_TableAdmin(admin.ModelAdmin):
    list_display = ('time')

class BreakUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'break_date', 'break_time')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'early_leave', 'late', 'absent')

class StudentRegisterAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'username', 'teacher')

admin.site.register(BreakUser, BreakUserAdmin)
admin.site.register(Break_Time_Table)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(StudentRegister, StudentRegisterAdmin)