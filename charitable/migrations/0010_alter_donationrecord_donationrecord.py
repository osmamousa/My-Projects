# Generated by Django 4.0.4 on 2022-04-23 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0009_alter_donationrecord_donationrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrecord',
            name='donationrecord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drecord', to='charitable.donationgoal'),
        ),
    ]
