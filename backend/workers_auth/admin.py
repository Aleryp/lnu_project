from django.contrib import admin
from workers_auth.models import LannisterUser


@admin.register(LannisterUser)
class LannisterUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")

