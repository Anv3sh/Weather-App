# Generated by Django 4.2.6 on 2023-10-19 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_rename_city_customsession_cities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customsession',
            old_name='session_ptr',
            new_name='session',
        ),
    ]