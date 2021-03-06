# Generated by Django 3.2.8 on 2021-10-22 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=256)),
                ('is_added_to_favourites', models.BooleanField()),
                ('file', models.FileField(null=True, upload_to='videos/')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('is_active_day', models.BooleanField()),
                ('categories', models.ManyToManyField(to='workout.Category')),
                ('equipment', models.ManyToManyField(to='workout.Equipment')),
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='workout.video')),
            ],
        ),
    ]
