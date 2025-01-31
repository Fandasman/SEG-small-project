# Generated by Django 3.2.5 on 2021-12-02 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20211130_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='experience',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('master', 'Master'), ('professional', 'Professional')], max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='The username must contain at least three character of any kind!', regex='^\\w{3,}$')]),
        ),
    ]
