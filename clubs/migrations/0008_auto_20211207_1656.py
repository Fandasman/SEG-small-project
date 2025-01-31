# Generated by Django 3.2.5 on 2021-12-07 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0007_clubmember_clubofficer_clubowner'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clubs.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClubOwner',
        ),
    ]
