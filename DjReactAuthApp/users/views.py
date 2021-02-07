from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def users_list(request):
    if request.method == 'GET':
        users=CustomUser.objects.all()
        serializers = CustomUserSerializer(users, many=True)
        return Response(serializers.data)
