# Generated by Django 4.2.2 on 2023-06-29 12:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0005_patrol_data"),
    ]

    operations = [
        migrations.RenameField(
            model_name="patrol_data",
            old_name="week_name",
            new_name="date",
        ),
    ]
