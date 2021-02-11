from rest_framework import serializers
from .models import CustomUser, UserProfile
from django.contrib.auth import authenticate
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator


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

    def validate(self, attrs):
        if len(attrs['password']) < 4:
            raise serializers.ValidationError("password must be greater than 4 chars")
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        is_old_password_correct = user.check_password(value)
        if not is_old_password_correct:
            raise serializers.ValidationError({"old_password": "incorrect old password"})
        return value

    def validate(self, attrs):
        if len(attrs['new_password']) < 4 or attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "new_password": "either new password is less than 4 chars or it doesnt matches with confirm password,Please enter a valid new password"})

        if attrs['new_password'] == attrs['old_password']:
            raise serializers.ValidationError({
                "new_password": "new password can not same as the old password, Please try again with a valid password"})
        return attrs


class RequestPasswordResetSerializers(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        is_user = CustomUser.objects.filter(email=value).exists()
        if not is_user:
            raise serializers.ValidationError("user doesn't exists with this email")
        return value


class SetNewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    uidb64 = serializers.CharField(required=True)

    def validate(self, attrs):
        if len(attrs['new_password'])<4 or attrs['new_password'] !=attrs['confirm_password']:
            raise serializers.ValidationError({
                "new_password": "either new password is less than 4 chars or it doesnt matches with confirm password,Please enter a valid new password"})
        return attrs

