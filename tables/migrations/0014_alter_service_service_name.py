# Generated by Django 4.0.5 on 2022-07-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0013_service_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='Service_name',
            field=models.CharField(max_length=100),
        ),
    ]
