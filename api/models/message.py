from django.conf import settings
from django.db import models
from api.utils.models import get_sentinel_user


class Message(models.Model):
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="messages",
        on_delete=models.SET(get_sentinel_user),
    )
    thread = models.ForeignKey(
        "api.Thread",
        related_name="messages",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("created_at", "-id")
