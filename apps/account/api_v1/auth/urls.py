from django.urls import path

from apps.account.api_v1.auth.views import (
    JWTTokenObtainPairView,
    JWTTokenRefreshView,
    JWTTokenVerifyView,
)


auth_urlpatterns = [
    path("jwt/create/", JWTTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", JWTTokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", JWTTokenVerifyView.as_view(), name="jwt-verify"),
]
