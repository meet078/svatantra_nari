# Generated by Django 4.0.4 on 2022-09-25 02:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default=datetime.datetime(2022, 9, 25, 2, 29, 52, 444827), upload_to='image'),
        ),
    ]