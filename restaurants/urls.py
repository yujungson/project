from django.urls import path
from . import views

app_name = "restaurants"

urlpatterns = [
    path("create/", views.CreateRestaurantView.as_view(), name="create"),
    path("<int:pk>", views.RestaurantDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditRestaurantView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.RestaurantPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add", views.AddPhotoView.as_view(), name="add-photo"),
    path(
        "<int:restaurant_pk>/photos/<int:photo_pk>/delete",
        views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:restaurant_pk>/photos/<int:photo_pk>/edit",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path("search/", views.SearchView.as_view(), name="search"),
]
