# Generated by Django 4.0.4 on 2022-06-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0004_movie_imdb_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="release_date",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]