# Generated by Django 4.1.7 on 2023-04-03 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inbox", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="broadcast",
            options={"verbose_name": "broadcast", "verbose_name_plural": "broadcasts"},
        ),
        migrations.AlterModelTable(
            name="broadcast",
            table="broadcast",
        ),
    ]