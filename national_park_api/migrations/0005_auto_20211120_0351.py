# Generated by Django 3.2.9 on 2021-11-20 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('national_park_api', '0004_attraction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attraction',
            options={'verbose_name': 'attraction', 'verbose_name_plural': 'attraction'},
        ),
        migrations.AlterField(
            model_name='attraction',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_attractions', to='national_park_api.nationalpark'),
        ),
    ]
