# Generated by Django 3.2.6 on 2021-09-28 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0007_auto_20210928_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 11, 54, 20, 66147)),
        ),
    ]
