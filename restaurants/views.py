from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
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
        form = forms.SearchForm()
        if form.is_valid():

            city = form.cleaned_data.get("city")
            service_options = form.cleaned_data.get("service_options")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            instant_book = form.cleaned_data.get("instant_book")
            superhost = form.cleaned_data.get("superhost")
            highlights = form.cleaned_data.get("highlights")
            accessibilities = form.cleaned_data.get("accessibilities")

            filter_args = {}

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            if service_options is not None:
                filter_args["service_options"] = service_options

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guests__gte"] = guests

            if instant_book is True:
                filter_args["instant_book"] = True

            if superhost is True:
                filter_args["host__superhost"] = True

            for highlight in highlights:
                filter_args["highlights"] = highlight

            for accessibility in accessibilities:
                filter_args["accessibilities"] = accessibility

            qs = models.Restaurant.objects.filter(**filter_args).order_by("-created")

            paginator = Paginator(qs, 10, orphans=5)

            page = request.GET.get("page", 1)

            restaurants = paginator.get_page(page)
            return render(
                request,
                "restaurants/search.html",
                {"form": form, "restaurants": restaurants},
            )

        else:
            form = forms.SearchForm()

        return render(request, "restaurants/search.html", {"form": form})


class EditRestaurantView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Restaurant
    template_name = "restaurants/restaurant_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
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
            messages.error(request, "Cant delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("restaurants:photos", kwargs={"pk": restaurant_pk}))
    except models.Restaurant.DoesNotExist:
        return redirect(reverse("core:home"))


class EditPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    model = models.Photo
    template_name = "restaurants/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
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
        messages.success(self.request, "Photo Uploaded")
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
