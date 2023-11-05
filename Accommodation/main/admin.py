from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from. import models
from . models import User

# Register your models here.
admin.site.register(models.Room)
  

admin.site.register(models.RoomApplication)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("name", 'room', 'id_num', 'status' )

admin.site.register(User, CustomUserAdmin)
