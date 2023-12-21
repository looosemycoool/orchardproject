from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField

class CustomUser(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=10, blank=True)
    is_teacher = models.BooleanField(default=False)  # 추가된 필드
    is_student = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    # student_number = models.CharField(max_length=10, blank=True)

class Break_Time_Table(models.Model):
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.time

class BreakUser(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    break_date = models.CharField(max_length=10)
    break_time = models.ForeignKey(Break_Time_Table, null=True, on_delete=models.CASCADE)