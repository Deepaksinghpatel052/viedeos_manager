# Generated by Django 3.0.4 on 2020-05-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200514_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsusers',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]