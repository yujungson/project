from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(
    models.ServiceOptions,
    models.Accessibility,
    models.Highlights,
    models.Offerings,
    models.DiningOptions,
    models.Amenities,
    models.Atmosphere,
    models.Crowd,
    models.Planning,
    models.Payments,
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "service_options",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "fields": (
                    "highlights",
                    "accessibilities",
                    "offerings",
                    "dining_options",
                    "amenities",
                    "atmosphere",
                    "crowd",
                    "planning",
                    "payments",
                )
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_highlights",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "service_options",
        "highlights",
        "accessibilities",
        "offerings",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city", "^host__username")

    filter_horizontal = ("highlights", "accessibilities", "offerings")

    def count_highlights(self, obj):
        return obj.highlights.count()

    count_highlights.short_description = "Highlights Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
