from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_company_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 30, 12, 2, 0, 885066)),
        ),
    ]
