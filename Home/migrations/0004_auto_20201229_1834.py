# Generated by Django 3.1.4 on 2020-12-29 23:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0003_reviewcomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviewComment',
            new_name='Visited',
        ),
    ]
