# Generated by Django 4.0.4 on 2022-06-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_operator_country_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='test',
            field=models.IntegerField(blank=True, default=4),
        ),
    ]