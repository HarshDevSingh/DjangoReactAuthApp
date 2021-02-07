from django.contrib import admin
from .models import CustomUser,UserProfile,Gender

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Gender)