from rest_framework import permissions, generics

from api.models import Thread
from api.serializers import ThreadSerializer, ThreadWriteSerializer


class ThreadListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Thread.objects.prefetch_related("participants").filter(participants=self.request.user)

    def perform_create(self, serializer):
        thread = serializer.save(created_by=self.request.user)
        thread.participants.add(self.request.user)

    def get_serializer_class(self):
        return ThreadWriteSerializer if self.request.method == 'POST' else ThreadSerializer

