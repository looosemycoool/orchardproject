from django.db import models
from django.contrib.auth.models import User

class Planner(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True)

    todo1_subject = models.CharField(max_length=10, blank=True, null=True)
    todo1_content = models.CharField(max_length=100, blank=True, null=True)
    todo2_subject = models.CharField(max_length=10, blank=True, null=True)
    todo2_content = models.CharField(max_length=100, blank=True, null=True)
    todo3_subject = models.CharField(max_length=10, blank=True, null=True)
    todo3_content = models.CharField(max_length=100, blank=True, null=True)
    todo4_subject = models.CharField(max_length=10, blank=True, null=True)
    todo4_content = models.CharField(max_length=100, blank=True, null=True)
    todo5_subject = models.CharField(max_length=10, blank=True, null=True)
    todo5_content = models.CharField(max_length=100, blank=True, null=True)
    todo6_subject = models.CharField(max_length=10, blank=True, null=True)
    todo6_content = models.CharField(max_length=100, blank=True, null=True)
    todo7_subject = models.CharField(max_length=10, blank=True, null=True)
    todo7_content = models.CharField(max_length=100, blank=True, null=True)
    todo8_subject = models.CharField(max_length=10, blank=True, null=True)
    todo8_content = models.CharField(max_length=100, blank=True, null=True)
    todo9_subject = models.CharField(max_length=10, blank=True, null=True)
    todo9_content = models.CharField(max_length=100, blank=True, null=True)
    todo10_subject = models.CharField(max_length=10, blank=True, null=True)
    todo10_content = models.CharField(max_length=100, blank=True, null=True)

    korean_lecture_study_hour = models.IntegerField(blank=True, null=True)
    korean_lecture_study_min = models.IntegerField(blank=True, null=True)
    korean_self_study_hour = models.IntegerField(blank=True, null=True)
    korean_self_study_min = models.IntegerField(blank=True, null=True)

    math_lecture_study_hour = models.IntegerField(blank=True, null=True)
    math_lecture_study_min = models.IntegerField(blank=True, null=True)
    math_self_study_hour = models.IntegerField(blank=True, null=True)
    math_self_study_min = models.IntegerField(blank=True, null=True)

    english_lecture_study_hour = models.IntegerField(blank=True, null=True)
    english_lecture_study_min = models.IntegerField(blank=True, null=True)
    english_self_study_hour = models.IntegerField(blank=True, null=True)
    english_self_study_min = models.IntegerField(blank=True, null=True)

    research_lecture_study_hour = models.IntegerField(blank=True, null=True)
    research_lecture_study_min = models.IntegerField(blank=True, null=True)
    research_self_study_hour = models.IntegerField(blank=True, null=True)
    research_self_study_min = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.username
