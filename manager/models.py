from django.db import models
from django.contrib.auth.models import User


class Student_Study_Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    week_name = models.CharField(max_length=255, null=True, blank=False)
    student_name = models.CharField(max_length=255)

    research1 = models.CharField(max_length=10, null=True, blank=True)
    research2 = models.CharField(max_length=10, null=True, blank=True)

    korean_lecture_study = models.IntegerField(null=True, blank=True, default=0)
    korean_self_study = models.IntegerField(null=True, blank=True, default=0)
    math_lecture_study = models.IntegerField(null=True, blank=True, default=0)
    math_self_study = models.IntegerField(null=True, blank=True, default=0)
    english_lecture_study = models.IntegerField(null=True, blank=True, default=0)
    english_self_study = models.IntegerField(null=True, blank=True, default=0)
    research1_lecture_study = models.IntegerField(null=True, blank=True, default=0)
    research1_self_study = models.IntegerField(null=True, blank=True, default=0)
    research2_lecture_study = models.IntegerField(null=True, blank=True, default=0)
    research2_self_study = models.IntegerField(null=True, blank=True, default=0)


class Patrol_Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=255, null=True, blank=False)
    student_name = models.CharField(max_length=255)

    k_ss_count = models.IntegerField(null=True, blank=True)
    k_il_count = models.IntegerField(null=True, blank=True)
    m_ss_count = models.IntegerField(null=True, blank=True)
    m_il_count = models.IntegerField(null=True, blank=True)
    e_ss_count = models.IntegerField(null=True, blank=True)
    e_il_count = models.IntegerField(null=True, blank=True)
    r_ss_count = models.IntegerField(null=True, blank=True)
    r_il_count = models.IntegerField(null=True, blank=True)
    plan = models.IntegerField(null=True, blank=True)
    mentoring = models.IntegerField(null=True, blank=True)
    question = models.IntegerField(null=True, blank=True)
    consulting = models.IntegerField(null=True, blank=True)
    sleep = models.IntegerField(null=True, blank=True)

    focus_three = models.IntegerField(null=True, blank=True)
    focus_two = models.IntegerField(null=True, blank=True)
    focus_one = models.IntegerField(null=True, blank=True)
    total_focus_count = models.IntegerField(null=True, blank=True)