# Generated by Django 4.0.4 on 2022-06-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_alter_partner_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='Zone',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
