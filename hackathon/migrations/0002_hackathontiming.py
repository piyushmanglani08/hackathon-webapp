# Generated by Django 2.2.6 on 2019-11-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HackathonTiming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_time', models.DateTimeField(blank=True)),
                ('registration_end_time', models.DateTimeField(blank=True)),
                ('preparation_time', models.DateTimeField(blank=True)),
                ('preparation_end_time', models.DateTimeField(blank=True)),
                ('category_start_time', models.DateTimeField(blank=True)),
                ('category_end_time', models.DateTimeField(blank=True)),
                ('problem_start_time', models.DateTimeField(blank=True)),
                ('problem_end_time', models.DateTimeField(blank=True)),
                ('event_start_time', models.DateTimeField(blank=True)),
                ('event_end_time', models.DateTimeField(blank=True)),
                ('final_start_time', models.DateTimeField(blank=True)),
                ('final_end_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]