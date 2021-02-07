from rest_framework import serializers
from .models import CustomUser, UserProfile, Gender


class UserProfileSerializer(serializers.ModelSerializer):
    gender = serializers.StringRelatedField(many=False)

    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'avatar', 'dob', 'gender')


class CustomUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'is_active', 'is_staff', 'is_superuser', 'profile')
