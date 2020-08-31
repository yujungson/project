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
        return obj.restaurants.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    """ Restaurant Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "city",
                    "address",
                    "service_options",
                    "guests",
                )
            },
        ),
        (
            "Menues",
            {
                "fields": (
                    "menu_1",
                    "price_1",
                    "menu_2",
                    "price_2",
                    "menu_3",
                    "price_3",
                    "menu_4",
                    "price_4",
                    "menu_5",
                    "price_5",
                )
            },
        ),
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
        "guests",
        "count_highlights",
        "count_photos",
        "total_rating",
    )

    list_filter = (
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

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
