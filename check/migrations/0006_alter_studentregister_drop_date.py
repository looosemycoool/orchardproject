# Generated by Django 4.2.2 on 2023-12-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("check", "0005_alter_studentregister_class_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentregister",
            name="drop_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
