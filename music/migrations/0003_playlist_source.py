# Generated by Django 4.0.2 on 2022-04-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_playlist_playlist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='source',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
