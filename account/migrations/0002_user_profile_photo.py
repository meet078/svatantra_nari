# Generated by Django 4.0.4 on 2022-09-25 01:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default=datetime.datetime(2022, 9, 25, 1, 23, 36, 723027, tzinfo=utc), upload_to='image'),
            preserve_default=False,
        ),
    ]
