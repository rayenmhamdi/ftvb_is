# Generated by Django 2.2.3 on 2019-07-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teams_players'),
        ),
        migrations.AddField(
            model_name='player',
            name='proof',
            field=models.ImageField(blank=True, null=True, upload_to='teams_players_proofs'),
        ),
    ]
