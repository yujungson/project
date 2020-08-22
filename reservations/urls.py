from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path(
        "<int:room>/<int:year>-<int:month>-<int:day>/",
        views.choose_time,
        name="choose-time",
    ),
    path(
        "<int:room>/<int:year>-<int:month>-<int:day>-<str:time>/",
        views.choose_numofguests,
        name="choose-numofguests",
    ),
    path(
        "<int:room>/<int:year>-<int:month>-<int:day>-<str:time>/<int:numOfGuests>",
        views.create,
        name="create",
    ),
    path("<int:room>/", views.reservation_detail, name="detail",),
    path("<int:room>/<str:verb>/", views.edit_reservation, name="edit"),
]
