from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.response import Response

from apps.account.api_v1.account.serializers.registration import (
    RegistrationSerializer,
    VerfyEmailSerializer,
    ResendCodeSerializer,
    LoginSerializer,
)
from apps.account.api_v1.auth.views import NoJSONAPIRendererMixin
from apps.account.models.users import CustomUser




class RegistrationView(NoJSONAPIRendererMixin, generics.GenericAPIView):
    queryset = CustomUser.objects.none()
    serializer_class = RegistrationSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivateEmailView(NoJSONAPIRendererMixin, generics.GenericAPIView):
    queryset = CustomUser.objects.none()
    serializer_class = VerfyEmailSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResendCodeOnEmailView(NoJSONAPIRendererMixin, generics.GenericAPIView):
    queryset = CustomUser.objects.none()
    serializer_class = ResendCodeSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(NoJSONAPIRendererMixin, generics.GenericAPIView):
    queryset = CustomUser.objects.none()
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = [
    "RegistrationSerializer",
    "ActivateEmailView",
    "ResendCodeOnEmailView",
    "LoginView",
]
