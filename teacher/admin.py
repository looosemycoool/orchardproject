from django.contrib import admin
from .models import Consulting

class ConsultingAdmin(admin.ModelAdmin):
    list_display = ('date', 'teacher_id', 'student_name', 'consulting_type', 'consulting_subject', 'consulting_content')
    search_fields = ["teacher_id_name", "student_name"]

admin.site.register(Consulting, ConsultingAdmin)