# Generated by Django 4.0.4 on 2022-04-23 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0002_donationgoal_goaltitle_volunteergoal_goaltitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationgoal',
            old_name='Interval',
            new_name='interval',
        ),
    ]
