from django.conf import settings
from django.db import models
from comments.models import Comment

from hashtags.models import HashTag
from likes.models import Likes


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    video = models.FileField(blank=False, upload_to='videos')
    message = models.TextField(blank=True, null=True)
    hash_tags = models.ManyToManyField(HashTag, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)
    likes = models.ManyToManyField(Likes, blank=True,related_name='post_likes')
    mentions = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name='post_mentions')
