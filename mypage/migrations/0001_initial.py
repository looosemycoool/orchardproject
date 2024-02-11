# Generated by Django 4.2.2 on 2024-02-06 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Planner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(null=True)),
                (
                    "todo1_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo1_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo2_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo2_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo3_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo3_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo4_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo4_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo5_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo5_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo6_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo6_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo7_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo7_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo8_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo8_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo9_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo9_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "todo10_subject",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "todo10_content",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "korean_lecture_study_hour",
                    models.IntegerField(blank=True, default=0),
                ),
                (
                    "korean_lecture_study_min",
                    models.IntegerField(blank=True, default=0),
                ),
                ("korean_self_study_hour", models.IntegerField(blank=True, default=0)),
                ("korean_self_study_min", models.IntegerField(blank=True, default=0)),
                ("math_lecture_study_hour", models.IntegerField(blank=True, default=0)),
                ("math_lecture_study_min", models.IntegerField(blank=True, default=0)),
                ("math_self_study_hour", models.IntegerField(blank=True, default=0)),
                ("math_self_study_min", models.IntegerField(blank=True, default=0)),
                (
                    "english_lecture_study_hour",
                    models.IntegerField(blank=True, default=0),
                ),
                (
                    "english_lecture_study_min",
                    models.IntegerField(blank=True, default=0),
                ),
                ("english_self_study_hour", models.IntegerField(blank=True, default=0)),
                ("english_self_study_min", models.IntegerField(blank=True, default=0)),
                (
                    "research_lecture_study_hour",
                    models.IntegerField(blank=True, default=0),
                ),
                (
                    "research_lecture_study_min",
                    models.IntegerField(blank=True, default=0),
                ),
                (
                    "research_self_study_hour",
                    models.IntegerField(blank=True, default=0),
                ),
                ("research_self_study_min", models.IntegerField(blank=True, default=0)),
                (
                    "username",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]