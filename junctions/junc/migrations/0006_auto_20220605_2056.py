# Generated by Django 3.2.13 on 2022-06-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junc', '0005_auto_20220605_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junction',
            name='add_info',
            field=models.TextField(blank=True, default='', max_length=110),
        ),
        migrations.AlterField(
            model_name='junction',
            name='needs',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
