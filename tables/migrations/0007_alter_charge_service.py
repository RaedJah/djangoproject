# Generated by Django 4.0.4 on 2022-06-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_alter_service_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='Service',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]