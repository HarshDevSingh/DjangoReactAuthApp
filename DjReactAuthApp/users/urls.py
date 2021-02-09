from django.urls import path,include
from .views import users_list,user_detail,RegisterAPIView,LoginAPIView
from knox import views as knox_views

urlpatterns = [
    path('api/users/', users_list,name="users-list"),
    path('api/users/<int:id>/', user_detail,name="users-detail"),
    path('api/auth/', include('knox.urls')),
    path('api/users/register/', RegisterAPIView.as_view(),name="users-register"),
    path('api/users/login/', LoginAPIView.as_view(), name="users-register"),

]