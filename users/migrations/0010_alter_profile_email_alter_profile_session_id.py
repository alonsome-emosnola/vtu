# Generated by Django 4.1.10 on 2023-09-01 13:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0009_alter_profile_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.ForeignKey(db_column='email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='session_id',
            field=models.CharField(db_column='session_ID', default=datetime.datetime(2023, 9, 1, 14, 13, 50, 545098), max_length=256),
        ),
    ]
