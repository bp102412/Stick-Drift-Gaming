# Generated by Django 3.1.1 on 2020-12-13 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blog', '0013_auto_20201213_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogposts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Blog.blogpost')),
            ],
        ),
    ]
