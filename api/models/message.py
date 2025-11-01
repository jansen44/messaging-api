from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="Deleted")[0]

class Message(models.Model):
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: change to soft delete
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="messages",
        on_delete=models.SET(get_sentinel_user),
    )
