from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='ep08_post_set')  # user.ep08_post_set.all()
    message = models.CharField(max_length=140)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

