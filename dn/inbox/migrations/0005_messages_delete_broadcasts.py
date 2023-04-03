# Generated by Django 4.1.7 on 2023-04-03 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0002_remove_team_admins_remove_team_members_team_admins_and_more"),
        ("inbox", "0004_broadcasts_test"),
    ]

    operations = [
        migrations.CreateModel(
            name="Messages",
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
                ("message", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[("notification", "Notification"), ("email", "Email")],
                        default="notification",
                        max_length=20,
                    ),
                ),
                (
                    "broadcaster",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="broadcaster",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "teams",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.team"
                    ),
                ),
            ],
            options={
                "verbose_name": "message",
                "db_table": "message",
            },
        ),
        migrations.DeleteModel(
            name="Broadcasts",
        ),
    ]
