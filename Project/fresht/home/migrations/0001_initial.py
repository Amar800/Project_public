# Generated by Django 5.0.1 on 2024-01-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('synopsis', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=20)),
                ('actors', models.CharField(max_length=200)),
                ('genre', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Horror', 'Horror'), ('Rom-Com', 'Rom-Com'), ('Romantic', 'Romantic'), ('Slice of life', 'Slice of life'), ('Drama', 'Drama'), ('Thriller', 'Thriller'), ('Sci-fi', 'Sci-fi'), ('Crime', 'Crime'), ('Comedy', 'Comedy'), ('Fantasy', 'Fantasy'), ('Animated', 'Animated')], max_length=20)),
                ('rating', models.CharField(max_length=4)),
                ('trailer', models.CharField(max_length=250)),
            ],
        ),
    ]