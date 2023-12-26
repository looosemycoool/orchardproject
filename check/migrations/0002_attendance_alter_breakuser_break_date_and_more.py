# Generated by Django 4.2.2 on 2023-12-22 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("check", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                ("early_leave", models.TimeField(null=True)),
                ("late", models.TimeField(null=True)),
                ("absent", models.BooleanField(null=True)),
                (
                    "time1",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time2",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time3",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time4",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time5",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time6",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time7",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time8",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time9",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time10",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time11",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time12",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time13",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time14",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time15",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
                (
                    "time16",
                    models.CharField(
                        blank=True, default=False, max_length=10, null=True
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="breakuser",
            name="break_date",
            field=models.CharField(
                choices=[
                    ("MON", "Monday"),
                    ("TUE", "Tuesday"),
                    ("WED", "Wednesday"),
                    ("THU", "Thursday"),
                    ("FRI", "Friday"),
                    ("SAT", "Saturday"),
                    ("SUN", "Sunday"),
                ],
                max_length=10,
            ),
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
        migrations.AddField(
            model_name="attendance",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="check.breakuser"
            ),
        ),
    ]
