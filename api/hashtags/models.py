from django.db import models

class HashTag(models.Model):
    text = models.CharField(max_length=25)

    def get_hash_tag(self):
        return f'#{self.text}'
