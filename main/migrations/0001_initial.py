# Generated by Django 4.0.5 on 2022-06-18 02:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lhbattery', models.IntegerField(default=0)),
                ('rhbattery', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Battery',
            },
        ),
        migrations.CreateModel(
            name='HandGesture',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('f1h1', models.IntegerField(default=0)),
                ('f2h1', models.IntegerField(default=0)),
                ('f3h1', models.IntegerField(default=0)),
                ('f4h1', models.IntegerField(default=0)),
                ('f5h1', models.IntegerField(default=0)),
                ('f1h2', models.IntegerField(default=0)),
                ('f2h2', models.IntegerField(default=0)),
                ('f3h2', models.IntegerField(default=0)),
                ('f4h2', models.IntegerField(default=0)),
                ('f5h2', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Hand Gesture',
            },
        ),
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Team Members',
            },
        ),
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset', models.BooleanField(default=False)),
                ('HandGesture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.handgesture')),
            ],
            options={
                'verbose_name_plural': 'Reset',
            },
        ),
        migrations.CreateModel(
            name='RelatedWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('handgesture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.handgesture')),
            ],
            options={
                'verbose_name_plural': 'Related Word',
            },
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_location', models.BooleanField(default=False)),
                ('emergency_number', models.CharField(default='911', max_length=100)),
                ('HandGesture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.handgesture')),
            ],
            options={
                'verbose_name_plural': 'Emergency',
            },
        ),
    ]
