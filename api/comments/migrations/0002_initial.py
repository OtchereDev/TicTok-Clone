# Generated by Django 4.0 on 2021-12-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to='likes.CommentLike'),
        ),
    ]
