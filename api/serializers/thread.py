from rest_framework import serializers
from django.contrib.auth import get_user_model
from api.models import Thread

class ThreadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]


class ThreadSerializer(serializers.ModelSerializer):
    created_by = ThreadUserSerializer(read_only=True)
    participants = ThreadUserSerializer(read_only=True, many=True) 

    class Meta:
        model = Thread
        fields = ["id", "title", "created_at", "created_by", "participants"]


class ThreadWriteSerializer(serializers.ModelSerializer):
    participants = ThreadUserSerializer(read_only=True, many=True) 

    participant_ids = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=get_user_model().objects.all(),
        many=True
    )

    def create(self, validated):
        author = validated["created_by"]
        users = validated["participant_ids"]
        title = validated.get("title", "")

        thread = Thread(title=title, created_by=author)
        thread.save()
        thread.participants.set(users)
        return thread

    class Meta:
        model = Thread
        fields = ["title", "participant_ids", "participants"]
