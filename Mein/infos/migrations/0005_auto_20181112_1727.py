# Generated by Django 2.1.3 on 2018-11-12 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0004_maininfo_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeinfo',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='gradeinfo',
            name='lon',
        ),
        migrations.AddField(
            model_name='gradeinfo',
            name='hpid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='infos.MainInfo'),
        ),
    ]
