from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics

from api.models import Message, Thread
from api.serializers import MessageSerializer


class MessageListCreate(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        thread_id = self.kwargs["thread_id"]
        thread = get_object_or_404(Thread, pk=thread_id, participants=self.request.user)
        return (
            Message.objects
            .filter(thread_id=thread.id)
            .select_related("author")
            .order_by("created_at")
        )

    def perform_create(self, serializer):
        thread_id = self.kwargs["thread_id"]
        thread = get_object_or_404(Thread, pk=thread_id, participants=self.request.user)
        serializer.save(author=self.request.user, thread=thread)

