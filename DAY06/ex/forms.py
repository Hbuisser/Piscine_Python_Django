from .models import Tip
from django import forms

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = [
            'content',
        ]