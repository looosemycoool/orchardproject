from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField

class StudentRegister(models.Model):
    student = models.CharField(max_length=10, null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_student_registers', null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_student_registers', null=True, blank=True)
    class_name = models.CharField(max_length=10, null=True, blank=True)
    class_num = models.CharField(max_length=10, null=True, blank=True)
    # phone = models.CharField(max_length=10, null=True)
    register_date = models.DateField(null=True, blank=True)
    drop_date = models.DateField(null=True, blank=True)
    is_dropped = models.BooleanField(default=False)

    # Monday
    mon8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    mon22 = models.CharField(max_length=10, null=True, blank=True, default=False)
    # Tuesday
    tue8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    tue22 = models.CharField(max_length=10, null=True, blank=True, default=False)
    # Wednesday
    wed8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    wed22 = models.CharField(max_length=10, null=True, blank=True, default=False)
    # Thursday
    thu8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    thu22 = models.CharField(max_length=10, null=True, blank=True, default=False)
    # Friday
    fri8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    fri22 = models.CharField(max_length=10, null=True, blank=True, default=False)
    # Saturday
    sat8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sat22 = models.CharField(max_length=10, null=True, blank=True, default=False)
    # Sunday
    sun8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    sun22 = models.CharField(max_length=10, null=True, blank=True, default=False)

    def __str__(self):
        return self.student
class Break_Time_Table(models.Model):
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.time

class BreakUser(models.Model):
    DAY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THR', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    user = OneToOneField(User, on_delete=models.CASCADE)
    break_date = models.CharField(max_length=10, choices=DAY_CHOICES)
    break_time = models.ForeignKey(Break_Time_Table, null=True, on_delete=models.CASCADE)

class Attendance(models.Model):
    user = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=True)
    day_of_week = models.CharField(max_length=3, blank=True, null=True)

    early_leave = models.TimeField(null=True)
    late = models.TimeField(null=True)
    absent = models.BooleanField(null=True)

    time8 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time9 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time10 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time11 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time12 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time13 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time14 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time15 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time16 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time17 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time18 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time19 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time20 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time21 = models.CharField(max_length=10, null=True, blank=True, default=False)
    time22 = models.CharField(max_length=10, null=True, blank=True, default=False)

    # def save(self, *args, **kwargs):
    #     if self.date:
    #         self.day_of_week = self.date.strftime('%a').upper()
    #
    #         weekday_prefix = self.day_of_week.lower()
    #         for i in range(8, 23):
    #             field_name = f'{weekday_prefix}{i}'
    #             setattr(self, field_name, self.time8)
    #     super(Attendance, self).save(*args, **kwargs)