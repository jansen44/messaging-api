from rest_framework import permissions, generics

from django.contrib.auth import get_user_model
from api.serializers import UserSerializer, UserUpdateSerializer


# List here is temporary to make debugging easier
class UserRegister(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserProfile(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        return UserUpdateSerializer if self.request.method == 'PUT' else UserSerializer


