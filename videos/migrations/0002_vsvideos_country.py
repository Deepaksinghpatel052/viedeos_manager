# Generated by Django 3.0.4 on 2020-05-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsvideos',
            name='Country',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]