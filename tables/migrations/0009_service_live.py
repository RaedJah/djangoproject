# Generated by Django 4.0.5 on 2022-06-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0008_alter_service_service_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='live',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]