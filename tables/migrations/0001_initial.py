# Generated by Django 4.0.4 on 2022-06-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Operator', models.CharField(max_length=100)),
                ('Service_type', models.CharField(max_length=8)),
                ('Service', models.CharField(max_length=100)),
            ],
        ),
    ]
