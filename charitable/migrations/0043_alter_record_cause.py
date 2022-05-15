# Generated by Django 3.2.13 on 2022-05-09 19:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0042_merge_0039_alter_record_cause_0041_auto_20220509_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='cause',
            field=models.CharField(blank=True, choices=[('Animals', 'Animals'), ('Arts Culture Humanities', 'Arts Culture Humanities'), ('Asian Rights', 'Asian Rights'), ('Black Rights', 'Black Rights'), ('Community Development', 'Community Development'), ('Education', 'Education'), ('Environmental', 'Environmental'), ('Health', 'Health'), ('Human and Civil Rights', 'Human and Civil Rights'), ('Human Services', 'Human Services'), ('International', 'International'), ('Latino Rights', 'Latino Rights'), ('Research and Public Policy', 'Research and Public Policy'), ('Religion', 'Religion'), ("Women's Rights", "Women's Rights")], max_length=200),
        ),
    ]