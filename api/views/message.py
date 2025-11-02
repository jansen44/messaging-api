from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics
from rest_framework.exceptions import ValidationError

from api.models import Message, Thread
from api.models.message import build_message_strpos_annotation
from api.serializers import MessageSerializer, MessageSearchResultSerializer


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


class MessageSearch(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSearchResultSerializer

    def get_queryset(self):
        thread_id = self.kwargs["thread_id"]

        q = (self.request.query_params.get("q") or "").strip()
        if not q:
            raise ValidationError({"q": "Query param 'q' is required."})

        get_object_or_404(Thread, pk=thread_id, participants=self.request.user)
        match_index = build_message_strpos_annotation(q)
        
        return (
            Message.objects
            .filter(thread_id=thread_id, content__icontains=q)
            .select_related("author")
            .annotate(match_index=match_index)
        )


