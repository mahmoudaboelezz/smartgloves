# Generated by Django 4.0.4 on 2022-06-26 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_handgesture_accelerometer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handgesture',
            name='gesture_name',
        ),
    ]