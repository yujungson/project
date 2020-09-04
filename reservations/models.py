from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from core import models as core_models


class BookedDay(core_models.TimeStampedModel):

    date = models.DateField()
    time = models.CharField(max_length=6, default="00:00")
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, _("Pending")),
        (STATUS_CONFIRMED, _("Confirmed")),
        (STATUS_CANCELED, _("Canceled")),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    date = models.DateField()

    time = models.CharField(max_length=6, default="00:00")

    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )

    numOfGuests = models.IntegerField(default=1)

    restaurant = models.ForeignKey(
        "restaurants.Restaurant", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.restaurant} - {self.date}"

    def in_progress(self):
        now = timezone.now().date()
        return now <= self.date

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        is_finished = now > self.date
        if is_finished:
            BookedDay.objects.filter(reservation=self).delete()
        return is_finished

    is_finished.boolean = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            date = self.date
            time = self.time
            existing_booked_day = BookedDay.objects.filter(
                date=date, time=time
            ).exists()
            if not existing_booked_day:
                super().save(*args, **kwargs)
                BookedDay.objects.create(date=date, time=time, reservation=self)
                return
        return super().save(*args, **kwargs)
