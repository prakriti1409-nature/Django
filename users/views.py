from rest_framework import generics
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class ProfileView(APIView):
    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "telegram_username": user.telegram_username
        })
