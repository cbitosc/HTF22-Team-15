# Generated by Django 4.1.2 on 2022-10-30 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_company_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 30, 12, 2, 15, 50042)),
        ),
    ]
