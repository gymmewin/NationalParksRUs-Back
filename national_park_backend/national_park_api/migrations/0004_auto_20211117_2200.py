# Generated by Django 3.2.9 on 2021-11-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_park_api', '0003_auto_20211117_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationalpark',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='nationalpark',
            name='image',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='nationalpark',
            name='location',
            field=models.CharField(max_length=500),
        ),
    ]