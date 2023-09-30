from django.contrib import admin

from .models import Men, Category
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.admin import UserAdmin

@admin.register(Men)
class MenAdmin(admin.ModelAdmin):
    list_display = ('title', "id", 'user_id', 'cat')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', "id")


# AbstractUser.REQUIRED_FIELDS = ["email",]
UserAdmin.list_display = ("username", "email", "first_name", "last_name", "is_staff", 'id')
UserAdmin.ordering = ('-id',)

# EMAIL_FIELD = "email"
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]


# "fields": (
                    # "is_active",
                    # "is_staff",
                    # "is_superuser",
                    # "groups",
                    # "user_permissions",