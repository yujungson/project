import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from restaurants import models as restaurant_models
from reviews import forms as review_forms
from . import models


class CreateError(Exception):
    pass


@login_required
def create(request, restaurant, year, month, day, time, numOfGuests):
    try:
        date_obj = datetime.datetime(year, month, day)
        restaurant = restaurant_models.Restaurant.objects.get(pk=restaurant)
        models.BookedDay.objects.get(
            date=date_obj, time=time, reservation__restaurant=restaurant
        )
        raise CreateError()
    except (restaurant_models.Restaurant.DoesNotExist, CreateError):
        messages.error(request, _("This is the time that has already been reserved."))
        return render(
            request,
            "reservations/choose_detail.html",
            {"restaurant": restaurant.pk, "year": year, "month": month, "day": day},
        )

    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            restaurant=restaurant,
            date=date_obj,
            time=time,
            numOfGuests=numOfGuests,
        )
        messages.success(request, _("Reserved Successfully"))
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


@login_required
def choose_detail(request, restaurant, year, month, day):
    if request.method == "POST":
        time = request.POST.get("time")
        numOfGuests = request.POST.get("numOfGuests")
        return redirect(
            reverse(
                "reservations:create",
                kwargs={
                    "year": year,
                    "month": month,
                    "day": day,
                    "time": time,
                    "numOfGuests": numOfGuests,
                    "restaurant": restaurant,
                },
            )
        )

    else:
        return render(
            request,
            "reservations/choose_detail.html",
            {"year": year, "month": month, "day": day, "restaurant": restaurant},
        )


def reservation_detail(request, pk):
    reservation = models.Reservation.objects.get(pk=pk)
    if not reservation or (
        reservation.guest != request.user
        and reservation.restaurant.host != request.user
    ):
        raise Http404()
    form = review_forms.CreateReviewForm()
    return render(
        request,
        "reservations/detail.html",
        {"reservation": reservation, "form": form},
    )


def edit_reservation(request, pk, verb):
    reservation = models.Reservation.objects.get_or_none(pk=pk)
    if not reservation or (
        reservation.guest != request.user
        and reservation.restaurant.host != request.user
    ):
        raise Http404()
    if verb == "confirm":
        reservation.status = models.Reservation.STATUS_CONFIRMED
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELED
        models.BookedDay.objects.filter(reservation=reservation).delete()
    reservation.save()
    messages.success(request, _("Reservation Updated"))
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))
