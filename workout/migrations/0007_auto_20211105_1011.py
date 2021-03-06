# Generated by Django 3.2.8 on 2021-11-05 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout', '0006_alter_video_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=200)),
                ('repetitions', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Exercises',
                'verbose_name_plural': 'Exercise',
            },
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['created_at'], 'verbose_name': 'Training', 'verbose_name_plural': 'Trainings'},
        ),
        migrations.RemoveField(
            model_name='training',
            name='day_number',
        ),
        migrations.RemoveField(
            model_name='training',
            name='is_active_day',
        ),
        migrations.RemoveField(
            model_name='training',
            name='video',
        ),
        migrations.AddField(
            model_name='training',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='description',
            field=models.CharField(default='Description', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='is_fixed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='training',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='training',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='exercise',
            name='training',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='workout.training'),
        ),
    ]
