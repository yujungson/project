import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from reviews import forms as review_forms
from . import models, forms


class CreateError(Exception):
    pass


@login_required
def create(request, room, year, month, day, time, numOfGuests):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(date=date_obj, time=time, reservation__room=room)
        raise CreateError("This is the time that has already been reserved.")
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request)
        return redirect(
            reverse(
                "reservations:choose-time",
                kwargs={"room": room.pk, "year": year, "month": month, "day": day},
            )
        )
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            date=date_obj,
            time=time,
            numOfGuests=numOfGuests,
        )
        print(reservation.pk)
        messages.success(request, "Reserved Successfully")
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


@login_required
def choose_time(request, room, year, month, day):
    if request.method == "POST":
        form = forms.NumberOfGuestsForm(request.POST)
        if form.is_valid():
            time = form.data["time"]
            numOfGuests = form.data["numOfGuests"]
            return HttpResponseRedirect(
                reverse(
                    "reservations:choose-time",
                    args=(year, month, day, time, room, numOfGuests),
                )
            )
    else:
        form = forms.NumberOfGuestsForm()


@login_required
def choose_numofguests(request, room, year, month, day, time):
    print(request.method)
    numOfGuests = request.POST["numOfGuests"]
    return HttpResponseRedirect(
        reverse(
            "reservations:choose-numofguests",
            args=(year, month, day, time, room, numOfGuests),
        )
    )


def reservation_detail(request, room):
    reservation = models.Reservation.objects.get(room=room)
    print(reservation)
    if not reservation or (
        reservation.guest != request.user and reservation.room.host != request.user
    ):
        raise Http404()
    form = review_forms.CreateReviewForm()
    return render(
        request, "reservations/detail.html", {"reservation": reservation, "form": form},
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

