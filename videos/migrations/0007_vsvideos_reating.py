# Generated by Django 3.0.6 on 2020-05-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20200528_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsvideos',
            name='Reating',
            field=models.IntegerField(default=0),
        ),
    ]
