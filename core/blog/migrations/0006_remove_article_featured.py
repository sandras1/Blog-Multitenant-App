# Generated by Django 3.2 on 2024-03-21 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20240321_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='featured',
        ),
    ]
