# Generated by Django 2.1.3 on 2018-11-05 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('hpid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('div', models.CharField(default='', max_length=300)),
                ('subject', models.CharField(default='', max_length=1000)),
                ('tel', models.CharField(default='', max_length=50)),
                ('etel', models.CharField(default='', max_length=50)),
                ('info', models.CharField(default='', max_length=300)),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('addr', models.CharField(default='', max_length=50)),
                ('emergency', models.CharField(default='', max_length=4)),
                ('limbs', models.CharField(default='', max_length=4)),
                ('pregnent', models.CharField(default='', max_length=4)),
                ('newborn', models.CharField(default='', max_length=4)),
                ('burn', models.CharField(default='', max_length=4)),
                ('dialysis', models.CharField(default='', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='SubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mondayStart', models.CharField(default='', max_length=10)),
                ('mondayEnd', models.CharField(default='', max_length=10)),
                ('tuesdayStart', models.CharField(default='', max_length=10)),
                ('tuesdayEnd', models.CharField(default='', max_length=10)),
                ('wednesdayStart', models.CharField(default='', max_length=10)),
                ('wednesdayEnd', models.CharField(default='', max_length=10)),
                ('thursdayStart', models.CharField(default='', max_length=10)),
                ('thursdayEnd', models.CharField(default='', max_length=10)),
                ('fridayStart', models.CharField(default='', max_length=10)),
                ('fridayEnd', models.CharField(default='', max_length=10)),
                ('saturdayStart', models.CharField(default='', max_length=10)),
                ('saturdayEnd', models.CharField(default='', max_length=10)),
                ('sundayStart', models.CharField(default='', max_length=10)),
                ('sundayEnd', models.CharField(default='', max_length=10)),
                ('holidayStart', models.CharField(default='', max_length=10)),
                ('holidayEnd', models.CharField(default='', max_length=10)),
                ('hpid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infos.MainInfo')),
            ],
        ),
    ]
