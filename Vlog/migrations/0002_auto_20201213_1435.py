# Generated by Django 3.1.1 on 2020-12-13 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vlogpost',
            name='type',
            field=models.CharField(choices=[('Vlog', 'Vlog')], default='Vlog', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='vlogpost',
            name='created',
            field=models.DateField(default=datetime.date.today, help_text='YYYY-MM-DD', verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='vlogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
