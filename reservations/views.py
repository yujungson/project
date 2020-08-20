import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from reviews import forms as review_forms
from . import models


class CreateError(Exception):
    pass


@login_required
def create(request, room, year, month, day, time):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(date=date_obj, time=time, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Can't Reserve That Room")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user, room=room, date=date_obj, time=time
        )
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


@login_required
def choose_time(request, room, year, month, day):
    lunchtime = ["11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00"]
    dinnertime = ["17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00"]
    return render(
        request,
        "reservations/choose_time.html",
        {
            "lunchtime": lunchtime,
            "dinnertime": dinnertime,
            "year": year,
            "month": month,
            "day": day,
            "room": room,
        },
    )


class ReservationDetailView(View):
    def get(self, *args, **kwargs):
        room_pk = kwargs.get("pk")
        reservation = models.Reservation.objects.get_or_none(pk=room_pk)
        print(reservation)
        if not reservation or (
            reservation.guest != self.request.user
            and reservation.room.host != self.request.user
        ):
            raise Http404()
        form = review_forms.CreateReviewForm()
        return render(
            self.request,
            "reservations/detail.html",
            {"reservation": reservation, "form": form},
        )


def edit_reservation(request, pk, verb):
    reservation = models.Reservation.objects.get_or_none(pk=pk)
    if not reservation or (
        reservation.guest != request.user and reservation.room.host != request.user
    ):
        raise Http404()
    if verb == "confirm":
        reservation.status = models.Reservation.STATUS_CONFIRMED
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELED
        models.BookedDay.objects.filter(reservation=reservation).delete()
    reservation.save()
    messages.success(request, "Reservation Updated")
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))

