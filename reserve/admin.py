from django.contrib import admin
from .models import Reserve, Time_Table, Teacher, Notice

class ReserveAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'teacher_id', 'student_name', 'title', 'comment', 'subject')
    search_fields = ["teacher_id__name", "student_name__first_name", "date"]

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'duty_day', 'duty_time')
    search_fields = ["name"]

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_header', 'notice_body')


admin.site.register(Reserve, ReserveAdmin)
admin.site.register(Time_Table)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Notice, NoticeAdmin)