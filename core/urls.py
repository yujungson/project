from django.urls import path

from restaurants import views as restaurant_views

app_name = "core"

urlpatterns = [
    path("", restaurant_views.HomeView.as_view(), name="home"),
]
