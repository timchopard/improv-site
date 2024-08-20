# Generated by Django 5.0.7 on 2024-08-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('photo', models.ImageField(upload_to='players/')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('tagline', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='shows/')),
                ('location', models.CharField(max_length=128)),
                ('postcode', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
