# Generated by Django 4.2.2 on 2023-08-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reserve", "0008_alter_reserve_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="retired",
            field=models.BooleanField(default=False),
        ),
    ]
