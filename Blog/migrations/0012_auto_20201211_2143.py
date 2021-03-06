# Generated by Django 3.1.1 on 2020-12-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_blogpost_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ['-date'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated',
            field=models.DateField(auto_now=True, null=True, verbose_name='Date Updated'),
        ),
    ]
