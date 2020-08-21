from django.utils import timezone
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from cal import Calendar


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ServiceOptions(AbstractItem):  # roomtype

    """ ServiceOptions Model Definition """

    class Meta:
        verbose_name = "Service Options"


class Highlights(AbstractItem):  # amenity

    """ Highlights Model Definition """

    class Meta:
        verbose_name_plural = "Highlights"


class Accessibility(AbstractItem):  # facility

    """ Accessibility Model Definition """

    pass

    class Meta:
        verbose_name_plural = "Accessibilities"


class Offerings(AbstractItem):  # houserule

    """ Offerings Model Definition """

    class Meta:
        verbose_name = "Offerings"


class DiningOptions(AbstractItem):

    """ DiningOptions Model Definition """

    class Meta:
        verbose_name = "DiningOptions"


class Amenities(AbstractItem):

    """ Amenities Model Definition """

    class Meta:
        verbose_name = "Amenities"


class Atmosphere(AbstractItem):

    """ Atmosphere Model Definition """

    class Meta:
        verbose_name = "Atmosphere"


class Crowd(AbstractItem):

    """ Crowd Model Definition """

    class Meta:
        verbose_name = "Crowds"


class Planning(AbstractItem):

    """ Planning Model Definition """

    class Meta:
        verbose_name = "Planning"


class Payments(AbstractItem):

    """ Payments Model Definition """

    class Meta:
        verbose_name = "Payments"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField(help_text="How many people will be staying?")
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    service_options = models.ForeignKey(
        "ServiceOptions", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    highlights = models.ManyToManyField("Highlights", related_name="rooms", blank=True)
    accessibilities = models.ManyToManyField(
        "Accessibility", related_name="rooms", blank=True
    )
    offerings = models.ManyToManyField("Offerings", related_name="rooms", blank=True)
    dining_options = models.ManyToManyField(
        "DiningOptions", related_name="rooms", blank=True
    )
    amenities = models.ManyToManyField("Amenities", related_name="rooms", blank=True)
    atmosphere = models.ManyToManyField("Atmosphere", related_name="rooms", blank=True)
    crowd = models.ManyToManyField("Crowd", related_name="rooms", blank=True)
    planning = models.ManyToManyField("Planning", related_name="rooms", blank=True)
    payments = models.ManyToManyField("Payments", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos

    def get_calendars(self):
        now = timezone.now()
        this_year = now.year
        this_month = now.month
        next_month = this_month + 1
        if this_month == 12:
            next_month = 1
        this_month_cal = Calendar(this_year, this_month)
        next_month_cal = Calendar(this_year, next_month)
        return [this_month_cal, next_month_cal]
