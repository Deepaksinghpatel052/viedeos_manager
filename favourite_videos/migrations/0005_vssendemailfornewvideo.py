# Generated by Django 3.0.6 on 2020-06-02 11:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_vsvideos_mail_send_status'),
        ('account', '0007_auto_20200514_2354'),
        ('favourite_videos', '0004_auto_20200602_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='VsSendEmailForNewVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Send_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Videos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VsVideos_SendEmailForNewVideo', to='videos.VsVideos')),
                ('VsUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_SendEmailForNewVideo', to='account.VsUsers')),
            ],
            options={
                'verbose_name_plural': 'VS Send Email For New Video Upload.',
            },
        ),
    ]
