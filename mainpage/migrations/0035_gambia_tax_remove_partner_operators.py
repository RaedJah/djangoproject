# Generated by Django 4.0.4 on 2022-06-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0034_alter_exchange_rate_rate_alter_partner_localcurrency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gambia_Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tax', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='partner',
            name='Operators',
        ),
    ]