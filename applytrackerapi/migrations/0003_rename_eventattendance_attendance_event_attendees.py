# Generated by Django 4.1.6 on 2023-02-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applytrackerapi', '0002_game_maker_game_number_of_players_game_skill_level'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventAttendance',
            new_name='Attendance',
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(through='applytrackerapi.Attendance', to='applytrackerapi.gamer'),
        ),
    ]