from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.models import Message, Thread


class MessageAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]


class MessageSerializer(serializers.ModelSerializer):
    author = MessageAuthorSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ["id", "content", "created_at", "author"]

