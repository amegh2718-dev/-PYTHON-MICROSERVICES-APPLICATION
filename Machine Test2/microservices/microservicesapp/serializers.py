from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import ActivityLog

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password',)  # Add other fields as needed
        extra_kwargs = {'password': {'write_only': True}}


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'
