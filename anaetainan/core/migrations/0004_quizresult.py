# Generated by Django 4.1.7 on 2024-08-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_delete_activitylog"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuizResult",
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
                ("nome", models.CharField(max_length=100)),
                ("time", models.CharField(max_length=100)),
                ("score", models.IntegerField()),
            ],
        ),
    ]
