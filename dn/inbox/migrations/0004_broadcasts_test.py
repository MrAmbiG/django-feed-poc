# Generated by Django 4.1.7 on 2023-04-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inbox", "0003_broadcasts_delete_broadcast"),
    ]

    operations = [
        migrations.AddField(
            model_name="broadcasts",
            name="test",
            field=models.BooleanField(default=False),
        ),
    ]
