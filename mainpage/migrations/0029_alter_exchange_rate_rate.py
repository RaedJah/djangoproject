# Generated by Django 4.0.4 on 2022-06-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0028_alter_exchange_rate_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange_rate',
            name='rate',
            field=models.DecimalField(decimal_places=5, max_digits=7),
        ),
    ]
