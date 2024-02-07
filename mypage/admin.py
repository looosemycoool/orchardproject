from django.contrib import admin
from .models import Planner

class PlannerAdmin(admin.ModelAdmin):
    list_display = ('username', 'date')
    search_fields = ["username__first_name", "date"]

admin.site.register(Planner, PlannerAdmin)