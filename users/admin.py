from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Custom Profile",
                {
                    "fields": (
                        "avatar",
                        "gender",
                        "bio",
                        "birthdate",
                        "language",
                        "login_method",
                    )
                },
            ),
        )
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "is_staff",
        "email_verified",
        "email_secret",
        "login_method",
    )
