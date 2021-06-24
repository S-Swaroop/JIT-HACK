# Generated by Django 3.2.4 on 2021-06-24 13:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.PositiveBigIntegerField(blank=True, default=0)),
                ('title', models.CharField(max_length=40)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=512)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('postconnect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
