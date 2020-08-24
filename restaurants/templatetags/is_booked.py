import datetime
from django import template
from reservations import models as reservation_models

register = template.Library()


@register.simple_tag
def is_booked(restaurant, date, time):
    if date.day == 0:
        return
    try:
        date = datetime.datetime(year=date.year, month=date.month, day=date.day)
        reservation_models.BookedDay.objects.get(
            date=date, time=time, reservation__restaurant=restaurant
        )
        return True
    except reservation_models.BookedDay.DoesNotExist:
        return False
