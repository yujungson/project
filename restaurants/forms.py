from django import forms
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(required=False)
    name = forms.CharField(initial="None", required=False)
    guests = forms.IntegerField(required=False)
    service_options = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.ServiceOptions.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    highlights = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Highlights.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    accessibilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Accessibility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    offerings = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Offerings.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    dining_options = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.DiningOptions.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenities.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    atmosphere = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Atmosphere.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    crowd = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Crowd.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    planning = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Planning.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    payments = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Payments.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        restaurant = models.Restaurant.objects.get(pk=pk)
        photo.restaurant = restaurant
        photo.save()


class CreateRestaurantForm(forms.ModelForm):
    class Meta:
        model = models.Restaurant
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

    def save(self, *args, **kwargs):
        restaurant = super().save(commit=False)
        return restaurant
