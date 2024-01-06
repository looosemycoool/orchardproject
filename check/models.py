from django.db import models
from django.contrib.auth.models import User

class StudentRegister(models.Model):
    student = models.CharField(max_length=10, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_student_registers', null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='username_student_registers', null=True, blank=True)
    class_name = models.CharField(max_length=10, null=True, blank=True)
    class_num = models.CharField(max_length=10, null=True, blank=True)

    student_phone = models.CharField(max_length=15, null=True, blank=True)
    parent_phone1 = models.CharField(max_length=15, null=True, blank=True)
    parent_phone2 = models.CharField(max_length=15, null=True, blank=True)

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

class Attendance(models.Model):
    user = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=True)
    day_of_week = models.CharField(max_length=3, blank=True, null=True)

    memo = models.TextField(max_length=2000, null=True, blank=True)
    early_leave = models.TimeField(null=True, blank=True)
    late = models.TimeField(null=True, blank=True)
    absent = models.BooleanField(null=True, blank=True, default=False)

    morning_late = models.TimeField(null=True, blank=True)
    lunch_late = models.TimeField(null=True, blank=True)
    night_late = models.TimeField(null=True, blank=True)

    morning_check = models.BooleanField(null=True, blank=True, default=False)
    lunch_check = models.BooleanField(null=True, blank=True, default=False)
    night_check = models.BooleanField(null=True, blank=True, default=False)

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

class PatrolCheck(models.Model):
    # student
    user = models.ForeignKey(StudentRegister, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=True)
    day_of_week = models.CharField(max_length=3, blank=True, null=True)
    # 08:20
    time1_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time1_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 08:50
    time2_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time2_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 09:40
    time3_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time3_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 10:10
    time4_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time4_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 11:20
    time5_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time5_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 11:50
    time6_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time6_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 13:40
    time7_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time7_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 14:10
    time8_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time8_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 15:00
    time9_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time9_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 15:30
    time10_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time10_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 16:30
    time11_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time11_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 17:00
    time12_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time12_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 19:30
    time13_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time13_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 20:00
    time14_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time14_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 21:00
    time15_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time15_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 21:30
    time16_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time16_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 22:25
    time17_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time17_focus = models.CharField(max_length=10, null=True, blank=True, default=False)
    # 23:25
    time18_study = models.CharField(max_length=10, null=True, blank=True, default=False)
    time18_focus = models.CharField(max_length=10, null=True, blank=True, default=False)

class Specify(models.Model):
    content = models.CharField(max_length=2000, null=True, blank=True)