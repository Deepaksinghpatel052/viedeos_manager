# Generated by Django 3.0.4 on 2020-05-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200514_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsusers',
            name='Zip_Code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
