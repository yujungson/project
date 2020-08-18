from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path(
        "create/<int:room>/<int:year>-<int:month>-<int:day>",
        views.create,
        name="create",
    ),
    path("<int:pk>/", views.ReservationDetailView.as_view(), name="detail"),
    path("<int:pk>/<str:verb>/", views.edit_reservation, name="edit"),
    path(
        "user/<int:pk>/",
        views.ShowUserReservationView.as_view(),
        name="user-reservation",
    ),
    path(
        "host/<int:pk>/",
        views.ShowHostReservationView.as_view(),
        name="host-reservation",
    ),
]
