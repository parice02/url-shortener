from django import forms

from app.models import Url


class URLForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ["long_form"]
        widgets = {
            "long_form": forms.TextInput(
                attrs={
                    "placeholder": "Entrez votre URL...",
                    "class": "form-control",
                }
            )
        }
