# Generated by Django 4.2.3 on 2023-07-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvpapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
