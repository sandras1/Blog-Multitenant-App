# Generated by Django 3.2 on 2024-03-21 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='featured',
        ),
    ]
