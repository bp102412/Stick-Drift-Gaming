# Generated by Django 3.1.1 on 2020-12-13 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vlog', '0002_auto_20201213_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vlogpost',
            name='image',
        ),
    ]