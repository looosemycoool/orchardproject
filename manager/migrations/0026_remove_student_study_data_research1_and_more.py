# Generated by Django 4.2.2 on 2024-01-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0025_alter_student_study_data_english_self_study_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student_study_data",
            name="research1",
        ),
        migrations.RemoveField(
            model_name="student_study_data",
            name="research2",
        ),
        migrations.AddField(
            model_name="student_study_data",
            name="research3_self_study",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name="student_study_data",
            name="research3_study",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]