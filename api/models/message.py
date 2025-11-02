from django.conf import settings
from django.db import models
from django.db.models import F, Value, IntegerField, ExpressionWrapper
from django.db.models.functions import Lower
from django.db.models.expressions import Func
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


def build_message_strpos_annotation(q):
    pos = Func(
        Lower(F("content")),
        Lower(Value(q)),
        function="STRPOS",
        output_field=IntegerField(),
    )
    return ExpressionWrapper(pos - Value(1), output_field=IntegerField())

