# Generated by Django 4.2 on 2023-04-07 14:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("company_api", "0003_auto_20230407_1607"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="worker",
            name="name",
        ),
    ]