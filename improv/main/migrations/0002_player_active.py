# Generated by Django 5.0.7 on 2024-08-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
