from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path(
        "<int:room>/<int:year>-<int:month>-<int:day>",
        views.choose_time,
        name="choose-time",
    ),
    path(
        "<int:room>/<int:year>-<int:month>-<int:day>-<str:time>",
        views.create,
        name="create",
    ),
    path("<int:pk>/", views.ReservationDetailView.as_view(), name="detail"),
    path("<int:pk>/<str:verb>/", views.edit_reservation, name="edit"),
]
