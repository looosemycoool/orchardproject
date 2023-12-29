from django.db import models
from django.contrib.auth.models import User


class Student_Study_Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    week_name = models.CharField(max_length=255, null=True, blank=False)
    student_name = models.CharField(max_length=255)

    research1 = models.CharField(max_length=10, null=True, blank=True)
    research2 = models.CharField(max_length=10, null=True, blank=True)

    korean_lecture_study = models.IntegerField(null=True, blank=True)
    korean_self_study = models.IntegerField(null=True, blank=True)
    math_lecture_study = models.IntegerField(null=True, blank=True)
    math_self_study = models.IntegerField(null=True, blank=True)
    english_lecture_study = models.IntegerField(null=True, blank=True)
    english_self_study = models.IntegerField(null=True, blank=True)
    research1_lecture_study = models.IntegerField(null=True, blank=True)
    research1_self_study = models.IntegerField(null=True, blank=True)
    research2_lecture_study = models.IntegerField(null=True, blank=True)
    research2_self_study = models.IntegerField(null=True, blank=True)
    total_study_time = models.IntegerField(null=True, blank=True)


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


class Patrol_Weekly_Data(models.Model):
    week_name = models.CharField(max_length=255, null=True, blank=False)
    week_start_date = models.CharField(max_length=255, null=True, blank=False)
    week_end_date = models.CharField(max_length=255, null=True, blank=False)
    student_name = models.CharField(max_length=255, null=True, blank=False)

    total_k_ss_count = models.IntegerField(null=True, blank=True)
    total_k_il_count = models.IntegerField(null=True, blank=True)
    total_m_ss_count = models.IntegerField(null=True, blank=True)
    total_m_il_count = models.IntegerField(null=True, blank=True)
    total_e_ss_count = models.IntegerField(null=True, blank=True)
    total_e_il_count = models.IntegerField(null=True, blank=True)
    total_r_ss_count = models.IntegerField(null=True, blank=True)
    total_r_il_count = models.IntegerField(null=True, blank=True)

    total_plan = models.IntegerField(null=True, blank=True)
    total_mentoring = models.IntegerField(null=True, blank=True)
    total_question = models.IntegerField(null=True, blank=True)
    total_consulting = models.IntegerField(null=True, blank=True)
    total_sleep = models.IntegerField(null=True, blank=True)
    total_focus_three = models.IntegerField(null=True, blank=True)
    total_focus_two = models.IntegerField(null=True, blank=True)
    total_focus_one = models.IntegerField(null=True, blank=True)
    total_focus_count = models.IntegerField(null=True, blank=True)


class Total_Weekly_Study_Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    week_name = models.CharField(max_length=255, null=True, blank=False)
    week_start_date = models.CharField(max_length=255, null=True, blank=False)
    week_end_date = models.CharField(max_length=255, null=True, blank=False)
    student_name = models.CharField(max_length=255)

    # 탐구 과목
    research1 = models.CharField(max_length=10, null=True, blank=True)
    research2 = models.CharField(max_length=10, null=True, blank=True)

    # student_study_data
    korean_lecture_study = models.IntegerField(null=True, blank=True)
    korean_self_study = models.IntegerField(null=True, blank=True)
    math_lecture_study = models.IntegerField(null=True, blank=True)
    math_self_study = models.IntegerField(null=True, blank=True)
    english_lecture_study = models.IntegerField(null=True, blank=True)
    english_self_study = models.IntegerField(null=True, blank=True)
    research1_lecture_study = models.IntegerField(null=True, blank=True)
    research1_self_study = models.IntegerField(null=True, blank=True)
    research2_lecture_study = models.IntegerField(null=True, blank=True)
    research2_self_study = models.IntegerField(null=True, blank=True)
    total_study_time = models.IntegerField(null=True, blank=True)

    # patrol_data
    total_k_ss_count = models.IntegerField(null=True, blank=True)
    total_k_il_count = models.IntegerField(null=True, blank=True)
    total_m_ss_count = models.IntegerField(null=True, blank=True)
    total_m_il_count = models.IntegerField(null=True, blank=True)
    total_e_ss_count = models.IntegerField(null=True, blank=True)
    total_e_il_count = models.IntegerField(null=True, blank=True)
    total_r_ss_count = models.IntegerField(null=True, blank=True)
    total_r_il_count = models.IntegerField(null=True, blank=True)

    total_plan = models.IntegerField(null=True, blank=True)
    total_mentoring = models.IntegerField(null=True, blank=True)
    total_question = models.IntegerField(null=True, blank=True)
    total_consulting = models.IntegerField(null=True, blank=True)
    total_sleep = models.IntegerField(null=True, blank=True)
    total_focus_three = models.IntegerField(null=True, blank=True)
    total_focus_two = models.IntegerField(null=True, blank=True)
    total_focus_one = models.IntegerField(null=True, blank=True)
    total_focus_count = models.IntegerField(null=True, blank=True)


class Average_Study_Data(models.Model):
    week_name = models.CharField(max_length=255, null=True, blank=False)
    korean_lecture_study_average = models.IntegerField(null=True, blank=True)
    korean_self_study_average = models.IntegerField(null=True, blank=True)
    math_lecture_study_average = models.IntegerField(null=True, blank=True)
    math_self_study_average = models.IntegerField(null=True, blank=True)
    english_lecture_study_average = models.IntegerField(null=True, blank=True)
    english_self_study_average = models.IntegerField(null=True, blank=True)
    research_lecture_study_average = models.IntegerField(null=True, blank=True)
    research_self_study_average = models.IntegerField(null=True, blank=True)

    total_lecture_study_average = models.IntegerField(null=True, blank=True)
    total_self_study_average = models.IntegerField(null=True, blank=True)

    total_study_average = models.IntegerField(null=True, blank=True)