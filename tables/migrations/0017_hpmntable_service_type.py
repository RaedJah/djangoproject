# Generated by Django 4.0.5 on 2022-07-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0016_hpmntable'),
    ]

    operations = [
        migrations.AddField(
            model_name='hpmntable',
            name='Service_type',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]