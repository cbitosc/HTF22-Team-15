# Generated by Django 4.1.2 on 2022-10-30 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_merge_20221030_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='role',
            field=models.CharField(default='Software Engineer', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 30, 13, 14, 43, 746045)),
        ),
    ]
