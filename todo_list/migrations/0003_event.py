# Generated by Django 3.2.6 on 2021-09-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_rename_item_list_item_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_location', models.CharField(max_length=200)),
                ('event_date', models.DateField(max_length=200)),
                ('event_remarks', models.CharField(max_length=200)),
            ],
        ),
    ]
