from django import forms
from shortener.models import Shortener


class ShortenerForm(forms.ModelForm):
    full_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = Shortener

        fields = ('full_url',)
