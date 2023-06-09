# Generated by Django 4.2 on 2023-05-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0002_alter_task_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("L", "Low"), ("M", "Medium"), ("H", "High")],
                default="L",
                max_length=2,
            ),
        ),
    ]
