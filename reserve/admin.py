from django.contrib import admin
from .models import Reserve, Time_Table, Teacher, Notice

class ReserveAdmin(admin.ModelAdmin):
    search_fields = ['']

admin.site.register(Reserve)
admin.site.register(Time_Table)
admin.site.register(Teacher)
admin.site.register(Notice)