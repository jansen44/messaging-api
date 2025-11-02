from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import EmailTokenObtainPairSerializer

class EmailTokenObtainPair(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
