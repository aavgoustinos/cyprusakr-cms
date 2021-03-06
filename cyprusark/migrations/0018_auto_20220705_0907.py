# Generated by Django 3.2.12 on 2022-07-05 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyprusark', '0017_alter_person_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creativework',
            name='typeof',
        ),
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.CharField(blank=True, choices=[('author', 'author'), ('accountablePerson', 'accountablePerson'), ('character', 'character'), ('copyrightHolder', 'copyrightHolder'), ('creator', 'creator'), ('editor', 'editor'), ('funder', 'funder'), ('maintainer ', 'maintainer'), ('artist ', 'artist'), ('colorist ', 'colorist'), ('inker ', 'inker'), ('penciler ', 'penciler'), ('illustrator ', 'illustrator')], default=None, max_length=30, null=True),
        ),
    ]
