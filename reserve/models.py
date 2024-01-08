from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    subject = models.CharField(max_length=10)
    duty_day = models.CharField(max_length=10, null=True, blank=True)
    duty_time = models.CharField(max_length=20, null=True, blank=True)
    retired = models.BooleanField(default=False)  # 추가된 필드

    def __str__(self):
        return self.name

class Time_Table(models.Model):
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.time

class Reserve(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(null=True)
    teacher_id = models.ForeignKey("Teacher", related_name="teacher", null=True, on_delete=models.CASCADE)
    time = models.ForeignKey(Time_Table, on_delete=models.CASCADE, null=True)
    student_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='reservations')
    # reserved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    subject = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    # title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.date) if self.date else ''

class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    notice_header = models.CharField(max_length=50, null=True, blank=True)
    notice_body = models.TextField(max_length=10000, null=True, blank=True)
    #
    # def __str__(self):
    #     return self.notice_header