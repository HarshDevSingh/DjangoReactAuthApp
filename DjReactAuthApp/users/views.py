from .serializers import (CustomUserSerializer,
                          RegisterSerializer,
                          LoginSerializer,
                          ChangePasswordSerializer,
                          RequestPasswordResetSerializers, SetNewPasswordSerializer)
from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from knox.models import AuthToken

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from .mailer import Util


# Create your views here.
@api_view(['GET'])
def users_list(request):
    try:
        if request.method == 'GET':
            users = CustomUser.objects.all()
            serializers = CustomUserSerializer(users, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def user_detail(request, id=None):
    try:
        if request.method == 'GET':
            if id is not None:
                try:
                    user = get_object_or_404(CustomUser, id=id)
                    serializers = CustomUserSerializer(user, many=False)
                    return Response(serializers.data, status=status.HTTP_200_OK)
                except:
                    return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                _, token = AuthToken.objects.create(user)
                user = get_object_or_404(CustomUser, email=user.email)
                user_serializer = CustomUserSerializer(user, many=False)
                return Response({"user": user_serializer.data,
                                 "token": token})
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data
                _, token = AuthToken.objects.create(user)
                user = get_object_or_404(CustomUser, email=user.email)
                user_serializer = CustomUserSerializer(user, many=False)
                return Response({"user": user_serializer.data, "token": token}, status=status.HTTP_200_OK)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({
                'message': 'Password updated successfully',
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestAPIView(generics.GenericAPIView):
    serializer_class = RequestPasswordResetSerializers

    def post(self, request, *args, **kwrgs):
        try:
            serializer = self.get_serializer(data=request.data)
            email = request.data.get('email')
            try:
                if serializer.is_valid(raise_exception=True):
                    try:
                        user = CustomUser.objects.get(email=email)
                        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                        token = PasswordResetTokenGenerator().make_token(user)
                        current_site = get_current_site(request).domain
                        password_reset_link = f'http://{current_site}/{uidb64}/{token}/'
                        subject = f'Hi {user.profile.first_name}, Here is your link to reset password.'
                        body = f'click below link to reset your password:\n{password_reset_link}'
                        email_data = {"subject": subject, "body": body, "to": user.email}
                        Util.send_email(data=email_data)
                        return Response(
                            {'success': f'Hey {user.profile.first_name if user.profile.first_name else ""}, '
                                        f'A password reset link has been sent to your email:{user.email}'},
                            status=status.HTTP_200_OK)
                    except:
                        return Response({"error": "failed to send password reset link"},
                                        status=status.HTTP_400_BAD_REQUEST)

            except:
                return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def post(self, request, *args, **kwrgs):
        try:
            serializer = self.get_serializer(data=request.data)
            try:
                if serializer.is_valid(raise_exception=True):
                    token = request.data.get('token')
                    uidb64 = request.data.get('uidb64')
                    new_password = request.data.get('new_password')
                    user_id = force_str(urlsafe_base64_decode(uidb64))
                    user = CustomUser.objects.get(id=user_id)
                    if not PasswordResetTokenGenerator().check_token(user, token):
                        return Response({"error": "Invalid or Expired token, Please request a new password reset link"},
                                        status=status.HTTP_400_BAD_REQUEST)
                    user.set_password(new_password)
                    user.save()
                    subject = f'Password changed successfully'
                    body = f'Hi {user.profile.first_name if user.profile.first_name else ""}, your password was changed successfully, please login with new password'
                    email_data = {"subject": subject, "body": body, "to": user.email}
                    Util.send_email(data=email_data)
                    return Response(
                        {'success': f'Hey {user.profile.first_name if user.profile.first_name else ""}, '
                                    f'your password was reset successfully!'},
                        status=status.HTTP_200_OK)
            except:
                return Response({"error": "failed to reset password"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
