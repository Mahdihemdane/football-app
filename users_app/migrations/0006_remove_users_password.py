# Generated by Django 4.2.2 on 2023-06-06 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0005_auto_20230521_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
    ]