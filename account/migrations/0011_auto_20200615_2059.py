# Generated by Django 3.0.6 on 2020-06-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200615_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vsusers',
            name='Contact_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
