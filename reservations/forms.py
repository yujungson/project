from django import forms
from .models import Reservation


class NumberOfGuestsForm(forms.Form):
    """
    lunchtime = ["11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00"]
    dinnertime = ["17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00"]
    """

    time = forms.ChoiceField(
        choices=[("11:00", "11:00"), ("11:30", "11:30"), ("12:00", "12:00")],
        widget=forms.RadioSelect,
    )

    numOfGuests = forms.IntegerField()

    class Meta:
        model = Reservation
        fields = "time, numOfGuests"

