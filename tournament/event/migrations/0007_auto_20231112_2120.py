# Generated by Django 2.2.6 on 2023-11-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20231112_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cover',
            field=models.ImageField(blank=True, help_text='Здесь вы можете загрузить обложку для мероприятия.', null=True, upload_to='media/events/'),
        ),
    ]
