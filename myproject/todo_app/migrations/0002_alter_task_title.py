# Generated by Django 4.2 on 2023-04-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task", name="title", field=models.CharField(max_length=100),
        ),
    ]
