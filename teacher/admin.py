from django.contrib import admin
from .models import Consulting

class ConsultingAdmin(admin.ModelAdmin):
    list_display = ('date', 'teacher_id', 'student_name')
    search_fields = ["student_name"]

admin.site.register(Consulting, ConsultingAdmin)
