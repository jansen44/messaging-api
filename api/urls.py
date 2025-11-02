from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views


urlpatterns = [
    path('token', views.EmailTokenObtainPair.as_view(), name='token_obtain_pair'),
    path('token/refresh', views.EmailTokenObtainPair.as_view(), name='token_refresh'),

    path("register", views.UserRegister.as_view()),
    path("profile", views.UserProfile.as_view()),

    path("threads", views.ThreadListCreate.as_view()),
    path("threads/<int:thread_id>/messages", views.MessageListCreate.as_view()),
    path("threads/<int:thread_id>/messages/search", views.MessageSearch.as_view()),
]

