from django.urls import path
from .views import users_list

urlpatterns = [
    path('api/users/', users_list,name="users-list"),
]