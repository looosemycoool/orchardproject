# Generated by Django 4.2.2 on 2023-07-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0011_patrol_weekly_data_student_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Total_Weekly_Study_Data",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("week_name", models.CharField(max_length=255, null=True)),
                ("week_start_date", models.CharField(max_length=255, null=True)),
                ("week_end_date", models.CharField(max_length=255, null=True)),
                ("student_name", models.CharField(max_length=255)),
                ("research1", models.CharField(blank=True, max_length=10, null=True)),
                ("research2", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "korean_lecture_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "korean_self_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "math_lecture_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "math_self_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "english_lecture_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "english_self_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "research1_lecture_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "research1_self_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "research2_lecture_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "research2_self_study",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("total_k_ss_count", models.IntegerField(blank=True, null=True)),
                ("total_k_il_count", models.IntegerField(blank=True, null=True)),
                ("total_m_ss_count", models.IntegerField(blank=True, null=True)),
                ("total_m_il_count", models.IntegerField(blank=True, null=True)),
                ("total_e_ss_count", models.IntegerField(blank=True, null=True)),
                ("total_e_il_count", models.IntegerField(blank=True, null=True)),
                ("total_r_ss_count", models.IntegerField(blank=True, null=True)),
                ("total_r_il_count", models.IntegerField(blank=True, null=True)),
                ("total_plan", models.IntegerField(blank=True, null=True)),
                ("total_mentoring", models.IntegerField(blank=True, null=True)),
                ("total_question", models.IntegerField(blank=True, null=True)),
                ("total_consulting", models.IntegerField(blank=True, null=True)),
                ("total_sleep", models.IntegerField(blank=True, null=True)),
                ("total_focus_three", models.IntegerField(blank=True, null=True)),
                ("total_focus_two", models.IntegerField(blank=True, null=True)),
                ("total_focus_one", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="patrol_weekly_data",
            name="week_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
