# Generated by Django 4.0.4 on 2022-06-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_handgesture_gesture_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='handgesture',
            name='accelerometer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='handgesture',
            name='gesture_name',
            field=models.CharField(help_text='Enter the gesture name', max_length=200),
        ),
    ]
