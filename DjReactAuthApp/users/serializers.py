from rest_framework import serializers
from .models import CustomUser, UserProfile, Gender
from django.contrib.auth import authenticate


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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user=authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
