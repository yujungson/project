from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path(
        "<int:restaurant>/<int:year>-<int:month>-<int:day>/",
        views.choose_detail,
        name="choose-detail",
    ),
    path(
        "<int:restaurant>/<int:year>-<int:month>-<int:day>-<str:time>/<int:numOfGuests>",
        views.create,
        name="create",
    ),
    path("<int:restaurant>/", views.reservation_detail, name="detail",),
    path("<int:restaurant>/<str:verb>/", views.edit_reservation, name="edit"),
]
