# Generated by Django 2.2.6 on 2023-10-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20231026_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover',
            field=models.ImageField(blank=True, help_text='Здесь вы можете загрузить обложку для мероприятия.', null=True, upload_to='event_covers/'),
        ),
    ]