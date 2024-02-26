# Generated by Django 5.0.2 on 2024-02-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuapp', '0002_remove_insuranceplan_riders_insuranceplan_rider1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='insuranceplan',
            name='rider1_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='insuranceplan',
            name='rider2_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='insuranceplan',
            name='rider3_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='insuranceplan',
            name='rider4_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='insuranceplan',
            name='rider5_amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
