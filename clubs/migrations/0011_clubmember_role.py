# Generated by Django 3.2.5 on 2021-12-12 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0010_alter_club_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubmember',
            name='role',
            field=models.CharField(choices=[('MEM', 'Member'), ('OFF', 'Officer'), ('OWN', 'Owner')], default='MEM', max_length=3),
        ),
    ]
