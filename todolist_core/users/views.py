from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from users.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from users.models import CustomUserManager
from users.serializers import RegisterSerializer
from users.permissions import CanEdit

from users.serializers import RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomView(APIView):
    permission_classes = [IsAuthenticated]


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUserManager.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [CanEdit]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)