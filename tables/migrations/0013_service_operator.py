# Generated by Django 4.0.5 on 2022-07-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0012_alter_charge_calculated'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='Operator',
            field=models.CharField(default='Qcell', max_length=100),
            preserve_default=False,
        ),
    ]
