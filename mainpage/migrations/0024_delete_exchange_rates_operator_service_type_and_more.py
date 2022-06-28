# Generated by Django 4.0.4 on 2022-06-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0023_alter_partner_country'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Exchange_Rates',
        ),
        migrations.AddField(
            model_name='operator',
            name='service_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='operator',
            name='country_id',
            field=models.CharField(default='ysl', max_length=50),
        ),
        migrations.AlterField(
            model_name='partner',
            name='Country',
            field=models.CharField(max_length=50),
        ),
    ]
