# Generated by Django 4.0.4 on 2022-06-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_partner_created_at_partner_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country_id', models.IntegerField()),
                ('standard_iot', models.CharField(max_length=1000)),
                ('diot', models.CharField(max_length=1000)),
                ('rp_currency', models.CharField(max_length=6)),
                ('mcc_mnc', models.FloatField()),
                ('service_type', models.CharField(max_length=255)),
                ('agreement_type', models.CharField(max_length=255)),
                ('tadig', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]