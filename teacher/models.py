from django.db import models
from django.contrib.auth.models import User
from reserve.models import Teacher, Reserve

class Consulting(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    teacher_id = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE, blank=True)
    student_name = models.CharField(max_length=10, null=True, blank=True)
    consulting_type = models.CharField(max_length=20, null=True, blank=True)
    consulting_subject = models.CharField(max_length=100, null=True, blank=True)
    consulting_content = models.TextField(max_length=2000, null=True, blank=True)