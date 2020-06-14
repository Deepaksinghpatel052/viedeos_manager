# Generated by Django 3.0.6 on 2020-05-30 06:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videos', '0007_vsvideos_reating'),
    ]

    operations = [
        migrations.CreateModel(
            name='VsHomePageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_Of_The_Day_Thumbnail', models.ImageField(blank=True, null=True, upload_to=home.models.user_directory_path_thumbnail)),
                ('Session_2_Title', models.CharField(max_length=500)),
                ('Session_2_description', models.TextField()),
                ('Session_2_Image', models.ImageField(blank=True, null=True, upload_to=home.models.user_directory_path_sessing_image)),
                ('Session_3_box_1_Title', models.CharField(max_length=500)),
                ('Session_3_box_1_description', models.TextField()),
                ('Session_3_box_1_Image', models.ImageField(blank=True, null=True, upload_to=home.models.user_directory_path_Session_3_box_1_Image)),
                ('Session_3_box_2_Title', models.CharField(max_length=500)),
                ('Session_3_box_2_description', models.TextField()),
                ('Session_3_box_2_Image', models.ImageField(blank=True, null=True, upload_to=home.models.user_directory_path_Session_3_box_2_Image)),
                ('Session_3_box_3_Title', models.CharField(max_length=500)),
                ('Session_3_box_3_description', models.TextField()),
                ('Session_3_box_3_Image', models.ImageField(blank=True, null=True, upload_to=home.models.user_directory_path_Session_3_box_3_Image)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Video_Of_The_Day', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Video_Of_The_Day_HomePageSettings', to='videos.VsVideos')),
                ('Videos_Of_The_Week', models.ManyToManyField(blank=True, related_name='Videos_Of_The_Week_HomePageSettings', to='videos.VsVideos')),
            ],
            options={
                'verbose_name_plural': 'VS Home Page Settings',
            },
        ),
    ]
