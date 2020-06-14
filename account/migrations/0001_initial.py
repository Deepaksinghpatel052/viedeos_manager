# Generated by Django 3.0.4 on 2020-05-14 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VsUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('Type', models.CharField(max_length=200)),
                ('Image', models.FileField(blank=True, null=True, upload_to='user_imsge/%Y/%m/%d')),
                ('DOJ', models.DateField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('Contact_no', models.IntegerField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'VS Users',
            },
        ),
    ]
