# Generated by Django 3.2.13 on 2022-05-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0038_rename_your_reminder_emailreminder_message'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='cause',
            constraint=models.UniqueConstraint(fields=('cause',), name='one_cause'),
        ),
    ]