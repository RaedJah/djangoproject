# Generated by Django 4.0.5 on 2022-07-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0018_alter_hpmntable_call_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='live_on',
            field=models.DateField(blank=True),
        ),
    ]