# Generated by Django 4.2.16 on 2024-10-10 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caves', '0005_alter_cave_cave_maps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cave',
            name='latitude',
            field=models.FloatField(help_text='Please enter the latitude coordinate\n         in the Decimal Degrees format (e.g., -20.102852)', validators=[django.core.validators.RegexValidator(regex='^[-]\\d{2}\\.\\d{6}$')]),
        ),
        migrations.AlterField(
            model_name='cave',
            name='longitude',
            field=models.FloatField(help_text='Please enter the longitude coordinate\n         in the Decimal Degrees format (e.g., -43.453612)', validators=[django.core.validators.RegexValidator(regex='^[-]\\d{2}\\.\\d{6}$')]),
        ),
    ]
