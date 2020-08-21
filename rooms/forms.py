from django import forms
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(required=False)
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    instant_book = forms.ChoiceField(
        choices=[("True", "POSSIBLE"), ("False", "IMPOSIBLE")],
        widget=forms.RadioSelect,
    )
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
        room = models.Room.objects.get(pk=pk)
        photo.room = room
        photo.save()


class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = (
            "name",
            "description",
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

    def save(self, *args, **kwargs):
        room = super().save(commit=False)
        return room
