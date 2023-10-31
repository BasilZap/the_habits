from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from users.apps import UsersConfig
from django.urls import path
from users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
