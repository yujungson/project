from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Restaurant
    paginate_by = 12
    paginate_orphans = 0
    ordering = "created"
    context_object_name = "restaurants"


class RestaurantDetail(DetailView):

    """ RestaurantDetail Definition """

    model = models.Restaurant


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        city = request.GET.get("city")
        city = str.capitalize(city)

        if city:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                name = form.cleaned_data.get("name")
                name = str.capitalize(name)
                guests = form.cleaned_data.get("guests", 0)
                service_options = form.cleaned_data.get("service_options")
                highlights = form.cleaned_data.get("highlights")
                accessibilities = form.cleaned_data.get("accessibilities")
                offerings = form.cleaned_data.get("offerings")
                dining_options = form.cleaned_data.get("dining_options")
                amenities = form.cleaned_data.get("amenities")
                atmospheres = form.cleaned_data.get("atmosphere")
                crowds = form.cleaned_data.get("crowd")
                plannings = form.cleaned_data.get("planning")
                payments = form.cleaned_data.get("payments")
                print(city)
                print(name)

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__contains"] = city

                if name != "None":
                    filter_args["name__contains"] = name

                if guests is not None:
                    filter_args["guests__lte"] = guests

                for service_option in service_options:
                    filter_args["service_options"] = service_option

                for highlight in highlights:
                    filter_args["highlights"] = highlight

                for accessibility in accessibilities:
                    filter_args["accessibilities"] = accessibility

                for offering in offerings:
                    filter_args["offerings"] = offering

                for dining_option in dining_options:
                    filter_args["dining_options"] = dining_option

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for atmosphere in atmospheres:
                    filter_args["atmosphere"] = atmosphere

                for crowd in crowds:
                    filter_args["crowd"] = crowd

                for planning in plannings:
                    filter_args["planning"] = planning

                for payment in payments:
                    filter_args["payments"] = payment

                restaurants = models.Restaurant.objects.filter(**filter_args)

                return render(
                    request,
                    "restaurants/search.html",
                    {"form": form, "restaurants": restaurants},
                )
        else:
            form = forms.SearchForm()

        return render(
            request,
            "restaurants/search.html",
            {"form": form},
        )


class EditRestaurantView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Restaurant
    template_name = "restaurants/restaurant_edit.html"
    fields = (
        "name",
        "description",
        "city",
        "address",
        "guests",
        "service_options",
        "highlights",
        "accessibilities",
        "offerings",
        "dining_options",
        "amenities",
        "atmosphere",
        "crowd",
        "planning",
        "payments",
        "menu_1",
        "price_1",
        "menu_2",
        "price_2",
        "menu_3",
        "price_3",
        "menu_4",
        "price_4",
        "menu_5",
        "price_5",
    )

    def get_object(self, queryset=None):
        restaurant = super().get_object(queryset=queryset)
        if restaurant.host.pk != self.request.user.pk:
            raise Http404()
        return restaurant


class RestaurantPhotosView(user_mixins.LoggedInOnlyView, DetailView):

    model = models.Restaurant
    template_name = "restaurants/restaurant_photos.html"

    def get_object(self, queryset=None):
        restaurant = super().get_object(queryset=queryset)
        if restaurant.host.pk != self.request.user.pk:
            raise Http404()
        return restaurant


@login_required
def delete_photo(request, restaurant_pk, photo_pk):
    user = request.user
    try:
        restaurant = models.Restaurant.objects.get(pk=restaurant_pk)
        if restaurant.host.pk != user.pk:
            messages.error(request, _("Can't delete that photo"))
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, _("Photo Deleted"))
        return redirect(reverse("restaurants:photos", kwargs={"pk": restaurant_pk}))
    except models.Restaurant.DoesNotExist:
        return redirect(reverse("core:home"))


class EditPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    model = models.Photo
    template_name = "restaurants/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = _("Photo Updated")
    fields = ("caption",)

    def get_success_url(self):
        restaurant_pk = self.kwargs.get("restaurant_pk")
        return reverse("restaurants:photos", kwargs={"pk": restaurant_pk})


class AddPhotoView(user_mixins.LoggedInOnlyView, FormView):

    template_name = "restaurants/photo_create.html"
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, _("Photo Uploaded"))
        return redirect(reverse("restaurants:photos", kwargs={"pk": pk}))


class CreateRestaurantView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateRestaurantForm
    template_name = "restaurants/restaurant_create.html"

    def form_valid(self, form):
        restaurant = form.save()
        restaurant.host = self.request.user
        restaurant.save()
        form.save_m2m()
        messages.success(self.request, "Restaurant Uploaded")
        return redirect(reverse("restaurants:detail", kwargs={"pk": restaurant.pk}))