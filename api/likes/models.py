from django.db import models
from django.conf import settings


class Likes(models.Model):
    liking_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey("post.Post", models.CASCADE, related_name='post_liked')


class CommentLike(models.Model):
    liking_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey("comments.Comment", models.CASCADE)
