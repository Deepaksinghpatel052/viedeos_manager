# Generated by Django 3.0.6 on 2020-05-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_vsvideos_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vsvideos',
            name='Publich_Status',
            field=models.BooleanField(default=False),
        ),
    ]