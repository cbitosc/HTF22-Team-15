# Generated by Django 4.1.2 on 2022-10-29 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='desc',
            field=models.CharField(default='Not available', max_length=500),
        ),
    ]