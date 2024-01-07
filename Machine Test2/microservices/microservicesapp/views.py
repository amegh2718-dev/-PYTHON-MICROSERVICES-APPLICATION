from contextvars import Token
# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
import random
import string
from rest_framework.views import APIView
from .models import ActivityLog
from .serializers import ActivityLogSerializer
from .serializers import CustomUserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class GenerateAPIKeyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        api_key = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
        user.api_key = api_key
        user.save()
        return Response({'api_key': api_key})

class LogRegistrationView(generics.CreateAPIView):
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, action='User Registration')

class LogLoginView(generics.CreateAPIView):
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, action='User Login')

class LogGenerateAPIKeyView(generics.CreateAPIView):
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, action='API Key Generation')

class PublicActivityLogListView(generics.ListAPIView):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
    permission_classes = [permissions.AllowAny]
