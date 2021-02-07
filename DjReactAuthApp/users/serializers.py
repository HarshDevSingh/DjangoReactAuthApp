from rest_framework import serializers
from .models import CustomUser, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer( read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_active', 'is_staff', 'is_superuser', 'profile')
