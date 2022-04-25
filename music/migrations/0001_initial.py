# Generated by Django 4.0.2 on 2022-04-25 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('song', models.CharField(blank=True, max_length=100)),
                ('artist', models.CharField(blank=True, max_length=100)),
                ('album', models.CharField(blank=True, max_length=100)),
                ('yt_link', models.CharField(blank=True, max_length=100)),
                ('sf_link', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
