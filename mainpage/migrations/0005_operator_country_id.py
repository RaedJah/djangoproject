# Generated by Django 4.0.4 on 2022-06-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_operator_ndcs_remove_operator_country_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='country_id',
            field=models.SmallIntegerField(default=1, verbose_name=1),
            preserve_default=False,
        ),
    ]
