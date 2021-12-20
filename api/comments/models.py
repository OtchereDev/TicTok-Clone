from django.db import models
from django.utils import timezone

from likes.models import CommentLike


class Comment(models.Model):
    message = models.TextField()
    likes = models.ManyToManyField(CommentLike, blank=True,related_name='comment_likes')
    created = models.DateTimeField(default=timezone.now)

    def comment_likes_count(self):
        return self.likes.all().count()
