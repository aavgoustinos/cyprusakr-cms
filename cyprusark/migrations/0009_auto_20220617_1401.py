# Generated by Django 3.1.7 on 2022-06-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyprusark', '0008_auto_20220615_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creativework',
            name='classification',
            field=models.CharField(blank=True, choices=[('Unknown', 'Unknown'), ('Drawing', 'Drawing'), ('Book', 'Book'), ('Map', 'Map'), ('Painting', 'Painting'), ('Photograph', 'Photograph'), ('Manuscript', 'Manuscript'), ('Poster', 'Poster'), ('Sculpture', 'Sculpture'), ('VisualArtwork', 'VisualArtwork'), ('ArchiveComponent', 'ArchiveComponent')], max_length=60, null=True),
        ),
    ]
