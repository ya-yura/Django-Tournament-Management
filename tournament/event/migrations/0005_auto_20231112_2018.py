# Generated by Django 2.2.6 on 2023-11-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cover',
            field=models.ImageField(blank=True, help_text='Здесь вы можете загрузить обложку для мероприятия.', null=True, upload_to='events/'),
        ),
    ]
