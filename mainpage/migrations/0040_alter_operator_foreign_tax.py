# Generated by Django 4.0.4 on 2022-06-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0039_alter_gambia_tax_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='foreign_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]
