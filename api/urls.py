from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views.user import UserRegister, UserProfile
from api.views.message import MessageListCreate


urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path("register", UserRegister.as_view()),
    path("profile", UserProfile.as_view()),

    path("message", MessageListCreate.as_view()),
]
