# Generated by Django 4.2.2 on 2023-06-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="age",
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]
