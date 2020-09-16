from django import forms
from django.utils.translation import gettext_lazy as _
from . import models


class CreateReviewForm(forms.ModelForm):
    accuracy = forms.IntegerField(label=_("accuracy"), max_value=5, min_value=1)
    communication = forms.IntegerField(
        label=_("communication"), max_value=5, min_value=1
    )
    cleanliness = forms.IntegerField(label=_("cleanliness"), max_value=5, min_value=1)
    location = forms.IntegerField(label=_("location"), max_value=5, min_value=1)
    taste = forms.IntegerField(label=_("taste"), max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "cleanliness",
            "location",
            "taste",
        )

    def save(self):
        review = super().save(commit=False)
        return review
