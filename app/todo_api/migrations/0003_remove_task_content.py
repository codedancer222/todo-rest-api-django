# Generated by Django 4.0 on 2023-04-20 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_task_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='content',
        ),
    ]
