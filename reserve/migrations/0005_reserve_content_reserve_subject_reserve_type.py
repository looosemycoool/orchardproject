# Generated by Django 4.2.2 on 2023-07-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reserve", "0004_remove_reserve_comment_content_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserve",
            name="content",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="reserve",
            name="subject",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="reserve",
            name="type",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
