# Generated by Django 3.2.12 on 2022-06-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyprusark', '0011_auto_20220617_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='media',
            field=models.CharField(blank=True, choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), ('unknown', 'Unknown')], default=None, max_length=30, null=True),
        ),
    ]
