# Generated by Django 3.0.8 on 2020-11-30 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0003_auto_20201201_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='birth_day',
            field=models.DateField(auto_now=True),
        ),
    ]
