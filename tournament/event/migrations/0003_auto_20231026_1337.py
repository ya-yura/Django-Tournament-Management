# Generated by Django 2.2.6 on 2023-10-26 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_participant_team_tournament'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='captain',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
