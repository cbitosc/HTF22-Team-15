# Generated by Django 4.1.2 on 2022-10-30 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_company_email_remove_company_phone_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='date',
        ),
    ]
