# Generated by Django 5.0.2 on 2024-02-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuapp', '0005_remove_insuranceplan_number_of_years_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=50, null=True),
        ),
    ]
