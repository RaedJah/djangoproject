# Generated by Django 4.0.5 on 2022-06-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0010_call_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AlterField(
            model_name='charge',
            name='calculated',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]