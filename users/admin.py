from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.utils.html import mark_safe


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    inlines = (PhotoInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            (
                "Custom Profile",
                {
                    "fields": (
                        "gender",
                        "self_introduction",
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


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"