from django.contrib import admin
from .models import CustomUser, Break_Time_Table, BreakUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'class_name', 'is_teacher', 'is_student', 'is_manager')

class Break_Time_TableAdmin(admin.ModelAdmin):
    list_display = ('time')

class BreakUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'break_date', 'break_time')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BreakUser, BreakUserAdmin)
admin.site.register(Break_Time_Table)