from django.db import models
from django.contrib.auth.models import User

class Planner(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True)

    korean_lecture_study = models.IntegerField(blank=True, default=0)
    korean_self_study = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.username
