# Generated by Django 4.0.4 on 2022-11-05 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCapture',
            fields=[
                ('video_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('_data', models.TextField(blank=True, db_column='data')),
            ],
        ),
    ]
