# Generated by Django 4.0.4 on 2022-04-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0011_user_annual_income_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='annual_income',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]