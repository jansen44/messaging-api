from django.conf import settings
from django.db import models
from api.utils.models import get_sentinel_user


class Thread(models.Model):
    title = models.CharField(max_length=1024, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="authored",
        on_delete=models.SET(get_sentinel_user),
    )
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="threads",
    )

