# Generated by Django 3.0.7 on 2020-07-08 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_cms_page', '0003_vscmspage_set_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vscmspage',
            old_name='keywork',
            new_name='keyword',
        ),
    ]