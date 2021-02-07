from django.urls import path
from .views import users_list,user_detail

urlpatterns = [
    path('api/users/', users_list,name="users-list"),
    path('api/users/<int:id>/', user_detail,name="users-detail"),
]