# Generated by Django 4.0 on 2021-12-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hashtags', '0001_initial'),
        ('comments', '0002_initial'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos')),
                ('message', models.TextField(blank=True, null=True)),
                ('comments', models.ManyToManyField(blank=True, to='comments.Comment')),
                ('hash_tags', models.ManyToManyField(blank=True, to='hashtags.HashTag')),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to='likes.Likes')),
            ],
        ),
    ]
