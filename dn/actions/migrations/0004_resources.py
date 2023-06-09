# Generated by Django 4.1.7 on 2023-04-01 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("actions", "0003_resource2_delete_resource"),
    ]

    operations = [
        migrations.CreateModel(
            name="resources",
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
                (
                    "resource",
                    models.CharField(
                        choices=[
                            ("gpu", "gpu"),
                            ("vm", "vm"),
                            ("baremetal", "baremetal"),
                            ("k8s", "k8s"),
                        ],
                        max_length=30,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "resources",
                "db_table": "resources",
                "managed": True,
            },
        ),
    ]
