from .serializers import CustomUserSerializer, RegisterSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from knox.models import AuthToken


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
