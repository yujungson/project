from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        "users.User", related_name="list", on_delete=models.CASCADE, null=True
    )
    restaurants = models.ManyToManyField(
        "restaurants.Restaurant", related_name="lists", blank=True
    )

    def __str__(self):
        return self.name

    def count_restaurants(self):
        return self.restaurants.count()

    count_restaurants.short_description = "Number of Restaurants"
