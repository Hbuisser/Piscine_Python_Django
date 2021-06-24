from django import forms

class ContactForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
