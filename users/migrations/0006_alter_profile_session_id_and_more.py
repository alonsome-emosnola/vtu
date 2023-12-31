# Generated by Django 4.1.10 on 2023-08-30 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_bio_profile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='session_id',
            field=models.CharField(db_column='session_ID', default=datetime.datetime(2023, 8, 30, 23, 8, 54, 66493), max_length=256),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallet_balance',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10),
        ),
    ]
